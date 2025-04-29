class Solution {
public:
    int getSum(int a, int b) {
        uint carry = (a & b) << 1;
        uint res = a ^ b;
        while (carry > 0) {
            uint tmp = carry;
            carry = (carry & res) << 1;
            res = res ^ tmp;
        }
        return res;
    }
};
