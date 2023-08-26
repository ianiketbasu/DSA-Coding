class Solution {

    /**
     * @param Integer[][] $pairs
     * @return Integer
     */
    function findLongestChain($pairs) {
        // Sort the pairs based on the second element
        usort($pairs, function($a, $b) {
            return $a[1] - $b[1];
        });

        $n = count($pairs);
        $dp = array_fill(0, $n, 1); // Initialize dynamic programming array

        for ($i = 1; $i < $n; $i++) {
            for ($j = 0; $j < $i; $j++) {
                if ($pairs[$i][0] > $pairs[$j][1]) {
                    $dp[$i] = max($dp[$i], $dp[$j] + 1);
                }
            }
        }

        return max($dp);
    }
}