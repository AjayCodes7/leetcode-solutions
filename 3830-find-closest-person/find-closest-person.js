/**
 * @param {number} x
 * @param {number} y
 * @param {number} z
 * @return {number}
 */
var findClosest = function(x, y, z) {
    const xSteps = Math.abs(x-z);
    const ySteps = Math.abs(y-z);
    if (xSteps === ySteps){
        return 0;
    }
    if (xSteps < ySteps){
        return 1;
    }
    else{
        return 2;
    }
};