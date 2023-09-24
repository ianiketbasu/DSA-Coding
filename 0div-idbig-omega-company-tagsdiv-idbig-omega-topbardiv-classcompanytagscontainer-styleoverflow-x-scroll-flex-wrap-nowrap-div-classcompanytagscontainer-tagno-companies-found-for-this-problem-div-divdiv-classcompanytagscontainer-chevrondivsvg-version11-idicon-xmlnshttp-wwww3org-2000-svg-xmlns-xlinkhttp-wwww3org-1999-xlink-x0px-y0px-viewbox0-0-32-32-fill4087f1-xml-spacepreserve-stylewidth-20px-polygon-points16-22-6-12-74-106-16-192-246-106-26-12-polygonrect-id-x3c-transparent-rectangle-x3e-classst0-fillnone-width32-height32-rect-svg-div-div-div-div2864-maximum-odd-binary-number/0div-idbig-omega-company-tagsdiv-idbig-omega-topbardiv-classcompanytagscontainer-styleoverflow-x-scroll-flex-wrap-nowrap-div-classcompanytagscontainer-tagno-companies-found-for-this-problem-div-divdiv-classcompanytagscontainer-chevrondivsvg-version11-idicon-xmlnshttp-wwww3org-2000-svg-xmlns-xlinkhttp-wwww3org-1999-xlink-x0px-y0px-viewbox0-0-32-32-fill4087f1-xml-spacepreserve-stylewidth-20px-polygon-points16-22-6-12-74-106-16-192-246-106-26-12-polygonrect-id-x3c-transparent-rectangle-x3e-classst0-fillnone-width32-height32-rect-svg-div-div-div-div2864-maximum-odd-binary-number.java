public class Solution {
    public String maximumOddBinaryNumber(String s) {
        int n = s.length();
        int countOne = 0;

        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '1') {
                countOne++;
            }
        }

        int countZero = n - countOne;

        // Create a StringBuilder to modify the string in place
        StringBuilder modifiedString = new StringBuilder(s);

        // Set '1's for the first countOne - 1 characters
        for (int i = 0; i < countOne - 1; i++) {
            modifiedString.setCharAt(i, '1');
        }

        // Set '0's for the next countZero characters
        for (int i = countOne - 1; i < n - 1; i++) {
            modifiedString.setCharAt(i, '0');
        }

        // Set the last character to '1'
        modifiedString.setCharAt(n - 1, '1');

        return modifiedString.toString();
    }
}
