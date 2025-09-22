/**
 * @param {number[]} nums
 * @return {number}
 */
var maxFrequencyElements = function(nums) {
    const result = {};
    for(const num of nums){
        if (num in result){
            result[num]++;
        } else{
            result[num] = 1;
        }
    }

    var sortable = [];
    for (var key in result) {
        sortable.push([key, result[key]]);
    }
    let ans = 0;
    sortable.sort(function(a, b) {
        return b[1] - a[1];
    });

    var bigNum = sortable[0][1];
    sortable.forEach((item)=>{
        if(item[1]==bigNum){
            ans += bigNum
        } else{
            return ans;
        }
    });
    return ans;
};