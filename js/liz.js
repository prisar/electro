function sum(x, y) {
    setTimeout(()=> {
    console.log("2");
}, 0);
    // console.log("sum ", x+y)
}
sum(2, 3);
setTimeout(()=> {
    console.log("1");
}, 0);

