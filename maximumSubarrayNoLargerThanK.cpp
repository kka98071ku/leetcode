#include <iostream>
#include <set>
#include <vector>

using namespace std;

/**
 * Given an array of integers A and an integer k, find a subarray that contains
 * the largest sum, subject to a constraint that the sum is less than k?
 *
 * GOOD question as a follow-up to the very simple case where there is no
 * constraints
 */
int maximumSubarrayNoLargerThanK(vector<int> &nums, int k) {
  if (nums.empty()) {
    return 0;
  }
  int maxSoFar = INT_MIN;
  int cumulateSum = 0;
  set<int> cumulateSet = {0};
  for (auto &it : nums) {
    cumulateSum += it;
    /**
     * we need to find the minimum cumulate sum x that satisfies the
     * constraints: (cumulateSum - x) <= k, which is equivalent to find the
     * mimum x >= cumulateSum - k
     */
    set<int>::iterator sit = cumulateSet.lower_bound(cumulateSum - k);
    if (sit != cumulateSet.end()) {
      maxSoFar = max(maxSoFar, cumulateSum - *sit);
    }
    cumulateSet.insert(cumulateSum);
  }
  return maxSoFar;
}

int main() {
  std::vector<int> v = {4, -4, 1, -1, 2};
  std::cout << maximumSubarrayNoLargerThanK(v, 1) << std::endl;
}
