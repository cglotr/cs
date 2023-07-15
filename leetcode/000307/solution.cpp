class NumArray {
public:
    NumArray(vector<int>& nums) {
        int n = nums.size();
        seg_tree.resize(2 * n);
        for (int i = 0; i < n; i++) {
            seg_tree[n + i] = nums[i];
        }
        for (int i = n - 1; i > 0; i--) {
            seg_tree[i] = seg_tree[2 * i] + seg_tree[2 * i + 1];
        }
    }
    
    void update(int index, int val) {
        int n = seg_tree.size() / 2;
        int i = n + index;
        seg_tree[i] = val;
        while (i > 1) {
            seg_tree[i / 2] = seg_tree[i] + seg_tree[i ^ 1];
            i = i / 2;
        }
    }
    
    int sumRange(int left, int right) {
        int n = seg_tree.size() / 2;
        int l = n + left;
        int r = n + right;
        int ans = 0;
        while (l <= r) {
            if (l & 1) {
                ans += seg_tree[l];
                l = (l + 1) / 2;
            } else {
                l = l / 2;
            }
            if ((r & 1) == 0) {
                ans += seg_tree[r];
                r = (r - 1) / 2;
            } else {
                r = r / 2;
            }
        }
        return ans;
    }
private:
    vector<int> seg_tree;
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * obj->update(index,val);
 * int param_2 = obj->sumRange(left,right);
 */
