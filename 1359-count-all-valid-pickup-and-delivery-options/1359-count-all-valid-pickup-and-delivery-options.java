class Solution {
    public int countOrders(int n) {
        return n > 0 ? (int)((long)countOrders(n - 1) * (n * 2 - 1) * n % ((long)1e9 + 7)) : 1;
    }
}