// Problem: https://leetcode.com/problems/find-the-count-of-numbers-which-are-not-special
// Runtime: 81 ms

class Solution {
    public int nonSpecialCount(int l, int r) {
        // theorem: a 'special' num is the square of a prime
        // proof: if n is prime, it only has 1 proper divisor
        //        if n is not a square, it has 2n + 1 != 2 divisors
        //        if n is a square of a composite number, it has 1, the sqrt, and the divisors of sqrt
        
        // so equivalent to finding number of primes btw sqrt(l), sqrt(r)
        int cnt = 0;
        for (int i = (int) Math.ceil(Math.sqrt(l)); i <= (int) Math.sqrt(r); i++) {
            if (this.isPrime(i)) {
                cnt++;
            }
        }
        System.out.println(cnt);
        return (r - l + 1) - cnt;
    }
    
    private boolean isPrime(int n) {
        if (n == 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}