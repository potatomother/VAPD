// .fill(0)  es6方法
// .join(0).split("")  之前的方法
function monkey(num) {
    var monkeys = new Array(num + 1)
        .join(0)
        .split("")
        .map(function(value, key) {
            return key + 1;
        })
    console.log(monkeys);
    return monkeys
}

function monkeyKing(n, m) {
    var monkey_num = monkey(n);
    console.log(monkey_num);
    // 只有一个编号时直接返回
    if (n == 1) {
        return monkey_num[0];
    }
    var i = 0;
    while (monkey_num.length - 2 in monkey_num) {
        console.log("start");
        console.log(monkey_num.length - 2 in monkey_num);
        console.log(monkey_num.length-2);
        console.log(monkey_num);
        if ((i + 1) % m == 0) {
            delete monkey_num[i];
        } else {
            monkey_num.push(monkey_num[i]);
            delete monkey_num[i];
        }
        console.log("end");
        console.log(monkey_num.length - 2 in monkey_num);
        console.log(monkey_num.length-2);
        console.log(monkey_num);
        i++;
    }
    return monkey_num[monkey_num.length - 1];
}
var monkey_index = monkeyKing(10, 3);
console.log(monkey_index);