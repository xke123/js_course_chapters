# Lesson 12 - Advanced Functions 知识点整理

这份笔记基于 `12_Lesson 12 - Advanced Functions.srt` 整理，并补充了初学者学习这一课时应该一起掌握的相关知识点。整体目标是把“函数的高级用法”整理成一份可以复习、回看视频、做项目时参考的笔记。

---

## 一、知识点大纲

### 1. 本课核心主题
- 复习函数基础：`00:01:53`
- 函数也是值 `functions are values`：`00:02:53`
- 把函数保存到变量里：`00:03:40`
- 匿名函数 `anonymous function`：`00:05:41`
- 函数声明与提升 `hoisting`：`00:06:12`
- 把函数保存到对象里，形成方法 `method`：`00:07:14`
- 把值传进函数：`00:09:08`
- 把函数传进函数：回调函数 `callback`：`00:10:16`
- `setTimeout`：`00:12:03`
- 同步代码与异步代码：`00:14:09`
- `setInterval` 与 `clearInterval`：`00:16:58`、`00:28:00`
- 用定时器改造石头剪刀布自动播放：`00:18:47`
- `forEach()`：`00:31:18`
- `forEach` 与 `for` 的取舍：`00:33:31`、`00:39:32`
- `forEach` 里如何“跳过”：`return`：`00:39:49`
- 箭头函数 `arrow function`：`00:42:02`
- 箭头函数的简写规则：`00:44:01`、`01:25:00`
- 在项目里何时用箭头函数、何时保留普通函数：`00:47:55`
- 对象中的简写方法语法：`00:51:03`
- `addEventListener`：`00:52:53`
- `removeEventListener`：`00:56:56`
- 事件对象 `event object` 与 `event.key`：`01:05:05`
- `querySelectorAll()`：`01:13:43`
- `filter()`：`01:19:01`
- `map()`：`01:22:53`
- 闭包 `closure`：`01:26:39`

### 2. 本课项目线索
- 用 `setInterval` 实现石头剪刀布自动对战
- 用布尔变量记录是否正在自动播放
- 用 `setInterval` 返回的 ID 停止自动播放
- 用 `forEach` 替换 Todo List 里的 `for` 循环
- 用箭头函数让回调代码更简洁
- 用 `addEventListener` 替换 HTML 里的 `onclick`
- 给按钮和键盘事件绑定监听器
- 用 `querySelectorAll` 为多个删除按钮绑定事件
- 理解删除按钮中的闭包为什么能拿到正确索引

### 3. 初学者必须掌握的重点
- 函数不只是“代码块”，它本身也是值
- 函数可以赋值、传参、存到对象里、作为返回值使用
- 回调函数本质上就是“传入另一个函数中的函数”
- `setTimeout` 和 `setInterval` 都是异步 API
- `forEach` 是遍历数组的常用方法
- 箭头函数常用于回调
- `addEventListener` 比 `onclick` 更灵活
- `filter` 用于筛选，`map` 用于转换
- 闭包是函数“记住外部值”的能力

---

## 二、本课整体理解

这一课的核心不是“学几个新语法”这么简单，而是开始让你建立一种更成熟的 JavaScript 思维：

> 函数不是只能被定义然后调用，函数本身也可以像数字、字符串一样被保存、传递和组合。

一旦接受这一点，很多后面的写法就都能看懂了：
- 回调函数
- 定时器
- 事件监听
- 数组方法
- 箭头函数
- 闭包

所以这节课其实是在帮你跨过一个门槛：

从“会写函数”  
进入  
“会把函数当数据来使用”

---

## 三、复习：普通函数基础

### 1. 定义函数

对应视频时间：`00:01:53`

```js
function greeting() {
  console.log('hello');
}
```

### 2. 调用函数

```js
greeting();
```

含义：
- 定义函数：告诉程序“以后这段代码可以重复使用”
- 调用函数：真正执行它

这一部分本课不是重点，但后面所有高级内容都建立在这个基础上。

---

## 四、函数也是值

### 1. 核心概念

对应视频时间：`00:02:53`

这一课最重要的一句话就是：

> 函数也是值。

前面你学过：
- 数字是值
- 字符串是值
- 布尔值是值
- 数组和对象也是值

现在新增：

- 函数也是值

这意味着只要某件事你能对“值”做，就通常也能对“函数”做。

比如：
- 存到变量里
- 存到对象里
- 作为参数传进去
- 作为返回值返回出来

---

### 2. 把函数保存到变量里

对应视频时间：`00:03:40`

```js
const function1 = function greeting() {
  console.log('hello2');
};
```

这说明：
- 变量 `function1` 里保存的是一个函数
- 这个函数以后可以通过变量名访问

调用方式：

```js
function1();
```

补充理解：
- 这里变量保存的不是“函数运行后的结果”
- 而是“函数本身”

这和下面这种是不同的：

```js
const result = greeting();
```

这里保存的是执行结果，不是函数本身。

---

### 3. 用 `typeof` 检查函数

对应视频时间：`00:04:41`

```js
console.log(typeof function1); // 'function'
```

这和数组不同：
- 数组 `typeof` 是 `"object"`
- 函数 `typeof` 是 `"function"`

所以函数在 JS 里是一种特殊的可调用值。

---

## 五、匿名函数 Anonymous Function

### 1. 什么是匿名函数

对应视频时间：`00:05:41`

```js
const function1 = function () {
  console.log('hello');
};
```

这个函数没有名字，所以叫匿名函数。

为什么可以省略名字？

因为现在已经有变量 `function1` 可以访问它了。

换句话说：

> 只要有别的方式能拿到这个函数，函数名就不一定必须存在。

---

### 2. 匿名函数常见场景

匿名函数非常常见，尤其在这些地方：
- 回调函数
- 事件监听
- 定时器
- 数组方法内部

因为这些场景里函数往往只是“临时用一次”，没必要单独起名。

---

## 六、函数声明与提升 Hoisting

### 1. 函数声明

对应视频时间：`00:06:12`

```js
function greeting() {
  console.log('hello');
}
```

这种写法叫函数声明 `function declaration`。

---

### 2. 提升是什么意思

对应视频时间：`00:06:12`

函数声明有一个特性叫提升：

```js
greeting();

function greeting() {
  console.log('hello');
}
```

这段代码也能运行。

原因是函数声明会被提升。

可以先简单理解为：

> JavaScript 在执行前，会先“认识”这个函数声明。

---

### 3. 为什么函数表达式不能这样

```js
function1();

const function1 = function () {
  console.log('hello');
};
```

这不行。

因为：
- 这里不是函数声明
- 而是“把函数存进变量”
- 变量在赋值之前，函数还不存在

所以本课强调：

> 提升主要适用于函数声明，不适用于把函数保存到变量里的这种写法。

---

### 4. 实际建议

字幕里的建议是合理的：
- 大的、主要的函数，普通函数写法更清晰，也有提升
- 短小的回调函数，箭头函数更方便

这是后面写项目时很常见的一种风格。

---

## 七、把函数保存到对象里：方法 Method

### 1. 函数可以作为对象属性

对应视频时间：`00:07:14`

```js
const object1 = {
  num: 2,
  fun: function () {
    console.log('hello3');
  }
};
```

这里对象里有两个属性：
- `num`
- `fun`

其中 `fun` 的值是一个函数。

---

### 2. 什么是方法

调用：

```js
object1.fun();
```

当一个函数被保存在对象里，并通过对象访问时，通常称为方法 `method`。

可以简单理解成：

> 方法就是“对象身上的函数”。

---

### 3. 为什么对象里经常有方法

因为对象经常表示某个“实体”，除了存数据，还会带行为。

例如：
- 用户对象有登录方法
- 商品对象有计算价格方法
- DOM 元素对象有 `addEventListener()` 方法

所以“对象 + 方法”是一种非常基础的组织代码方式。

---

## 八、值作为参数，函数也可以作为参数

### 1. 传普通值

对应视频时间：`00:09:08`

```js
function display(param) {
  console.log(param);
}

display(2);
```

这里 `2` 被传给参数 `param`。

参数可以理解成：

> 函数内部临时用来接收外部值的变量。

---

### 2. 传函数进去

对应视频时间：`00:10:16`

```js
function run(param) {
  param();
}

run(function () {
  console.log('hello4');
});
```

这里：
- 外面传进去的是一个函数
- `run` 里通过 `param()` 把它调用了

---

### 3. 回调函数 Callback

对应视频时间：`00:11:42`

传进去的这个函数就叫回调函数 `callback`。

本质定义：

> 回调函数就是作为参数传给另一个函数的函数。

以后你会在很多地方看到回调：
- `setTimeout(() => {})`
- `addEventListener('click', () => {})`
- `array.forEach((value) => {})`
- `filter` / `map`

所以这一节非常关键。

---

## 九、`setTimeout`

### 1. 基本用法

对应视频时间：`00:12:03`

```js
setTimeout(function () {
  console.log('timeout');
}, 3000);
```

含义：
- 第一个参数：未来要执行的函数
- 第二个参数：等待时间，单位是毫秒

换算：
- `1000ms = 1s`
- `3000ms = 3s`

---

### 2. `setTimeout` 的本质

它的作用是：

> 先设置一个计时器，时间到了再执行回调函数。

注意，这不是“卡住 3 秒后再继续执行后面的代码”，而是“把任务登记一下，先继续往下走”。

这就引出了同步与异步。

---

## 十、同步代码与异步代码

### 1. 同步代码

对应视频时间：`00:14:09`

同步代码的特点：

> 一行做完，再做下一行。

大部分你写的普通 JS 代码都是同步的。

例如：

```js
console.log('a');
console.log('b');
```

输出顺序一定是：

```js
a
b
```

---

### 2. 异步代码

对应视频时间：`00:14:09`

看这个例子：

```js
setTimeout(function () {
  console.log('timeout');
}, 3000);

console.log('next line');
```

输出会先看到：

```js
next line
```

3 秒后才看到：

```js
timeout
```

原因是：
- `setTimeout` 不会阻塞后面的代码
- 它只是安排“将来再执行”

这就是异步。

---

### 3. 初学者应该怎么理解异步

可以先简单记成：

> 同步：排队做  
> 异步：先登记，后执行

这一课你不需要一下子理解事件循环的全部细节，但至少要知道：
- `setTimeout` 是异步
- 定时器回调是稍后执行的
- 后面的同步代码不会等它

---

## 十一、`setInterval` 与 `clearInterval`

### 1. `setInterval`

对应视频时间：`00:16:58`

```js
setInterval(function () {
  console.log('interval');
}, 3000);
```

作用：

> 每隔一段时间重复执行一次函数。

和 `setTimeout` 的区别：
- `setTimeout`：执行一次
- `setInterval`：反复执行

---

### 2. `setInterval` 也是异步的

对应视频时间：`00:18:22`

它和 `setTimeout` 一样，不会阻塞后面的代码。

---

### 3. `setInterval` 的返回值

对应视频时间：`00:28:00`

本课项目里强调了一个关键点：

```js
const intervalId = setInterval(function () {
  console.log('playing');
}, 1000);
```

`setInterval` 会返回一个 ID。

这个 ID 用来停止定时器。

---

### 4. `clearInterval`

对应视频时间：`00:28:00`

```js
clearInterval(intervalId);
```

作用：

> 停止对应的 interval。

这是本课项目自动播放功能能“再次点击停止”的关键。

---

## 十二、项目：石头剪刀布自动播放

### 1. 项目目标

对应视频时间：`00:18:47`

点击“Autoplay”后：
- 每秒自动玩一次
- 再点一次停止

这是本课第一个完整项目应用。

---

### 2. 自动播放的核心逻辑

对应视频时间：`00:24:25`

用 `setInterval` 每秒执行一次：

```js
intervalId = setInterval(function () {
  const playerMove = pickComputerMove();
  playGame(playerMove);
}, 1000);
```

思路：
- 电脑随机出拳
- 直接拿这个随机结果去调用 `playGame`

---

### 3. 用布尔值记录状态

对应视频时间：`00:26:31`

```js
let isAutoPlaying = false;
```

然后点击按钮时：
- 如果当前没在播放，就开始播放
- 如果当前正在播放，就停止播放

这是一种非常常见的状态管理思路。

---

### 4. 为什么 `intervalId` 要定义在函数外部

对应视频时间：`00:28:31`

因为每次点击按钮，函数都会重新执行。

如果把 `intervalId` 定义在函数内部：
- 每次都会是一个新的局部变量
- 上一次的 ID 就拿不到了

所以要写成：

```js
let intervalId;
```

放在函数外面，才能跨多次点击保留住它。

这实际上也和后面的闭包思维有点联系。

---

## 十三、`forEach()`

### 1. 基本概念

对应视频时间：`00:31:18`

`forEach()` 是数组的一个方法，用来遍历数组。

```js
['make dinner', 'wash dishes', 'watch youtube'].forEach(function (value) {
  console.log(value);
});
```

---

### 2. 它是怎么工作的

对应视频时间：`00:32:01`

`forEach` 会：
- 取数组第一个值
- 放进参数里
- 执行函数
- 再取第二个值
- 再执行函数
- 直到全部处理完

所以你可以把它理解为：

> 数组自己帮你完成循环。

---

### 3. 第二个参数：索引

对应视频时间：`00:33:31`

```js
arr.forEach(function (value, index) {
  console.log(value, index);
});
```

第二个参数是当前元素的索引。

---

### 4. `forEach` 与普通 `for` 的取舍

对应视频时间：`00:33:31`、`00:39:32`

本课建议：
- 普通遍历数组时，更推荐 `forEach`
- 因为可读性更强

但不是所有情况都适合 `forEach`：
- 如果需要 `break`，普通 `for` 更合适
- 如果只是对每项做处理，`forEach` 很舒服

这个判断在实际开发里很常见。

---

## 十四、把 Todo List 的 `for` 循环换成 `forEach`

### 1. 项目意义

对应视频时间：`00:34:28` 到 `00:39:32`

这一段不是新语法本身最重要，而是让你看到：

> 同一个逻辑可以用更合适的数组方法表达。

这说明：
- JS 循环不只有 `for`
- 项目代码可以不断重构得更清晰

---

### 2. 典型结构

```js
todoList.forEach(function (todoObject, index) {
  // 处理每个 todo
});
```

对比 `for`：
- 不用自己写初始化、条件、递增
- 直接关注“每一项要做什么”

---

## 十五、`forEach` 里如何“跳过”

### 1. 用 `return` 模拟 `continue`

对应视频时间：`00:39:49`

`forEach` 没有 `continue`，但可以这样：

```js
arr.forEach(function (value) {
  if (value === 'wash dishes') {
    return;
  }

  console.log(value);
});
```

这里 `return` 的作用是：
- 结束当前这次回调函数
- 进入下一项

效果和 `continue` 很像。

---

### 2. 为什么没有简单的 `break`

对应视频时间：`00:40:57`

字幕明确提到：

> `forEach` 不适合做提前中断。

如果你需要 `break`：
- 更适合用 `for`

这是一条非常实用的经验。

---

## 十六、箭头函数 Arrow Function

### 1. 基本写法

对应视频时间：`00:42:02`

```js
const arrowFunction = () => {
  console.log('hello');
};
```

调用方式和普通函数一样：

```js
arrowFunction();
```

---

### 2. 它和普通函数的关系

对应视频时间：`00:43:16`

箭头函数和普通函数在很多简单场景下作用类似：
- 都能接收参数
- 都能执行代码
- 都能返回值

但箭头函数通常更短，尤其适合短小回调。

---

### 3. 带参数的箭头函数

对应视频时间：`00:44:01`

```js
const oneParam = (param) => {
  console.log(param);
};

const twoParams = (a, b) => {
  console.log(a, b);
};
```

---

### 4. 返回值

对应视频时间：`00:44:01`

```js
const plus = (a, b) => {
  return a + b;
};
```

---

## 十七、箭头函数的简写规则

### 1. 一个参数时，可以省略括号

对应视频时间：`00:45:00`、`01:25:00`

```js
const double = value => {
  return value * 2;
};
```

---

### 2. 只有一行代码时，可以写成一行

```js
const double = value => value * 2;
```

---

### 3. 隐式返回

对应视频时间：`01:25:00`

当箭头函数只有一行表达式时：
- 可以省略 `{}` 和 `return`
- 表达式结果会自动返回

```js
const double = value => value * 2;
```

等价于：

```js
const double = value => {
  return value * 2;
};
```

---

### 4. 为什么这在数组方法里特别常见

因为 `forEach` / `filter` / `map` 往往只需要一个很短的回调函数。

所以你以后会经常看到这种写法：

```js
arr.map(value => value * 2);
```

---

## 十八、在项目里何时用箭头函数，何时保留普通函数

### 1. 回调里优先考虑箭头函数

对应视频时间：`00:47:55`

比如：
- `setInterval(() => {})`
- `forEach((value) => {})`
- `addEventListener('click', () => {})`

因为这些函数：
- 短
- 临时
- 就地使用

所以箭头函数更自然。

---

### 2. 主要功能函数可以保留普通函数

对应视频时间：`00:48:41`

例如：

```js
function autoPlay() {
  ...
}
```

课程给出的理由有两个：
- 更容易读
- 有提升

这个建议很实用。

初学阶段可以先按这个风格：
- 主函数：普通函数
- 回调函数：箭头函数

---

## 十九、对象中的简写方法语法

### 1. 普通写法

对应视频时间：`00:51:03`

```js
const obj = {
  method: function () {
    console.log('hello');
  }
};
```

### 2. 简写写法

```js
const obj = {
  method() {
    console.log('hello');
  }
};
```

这叫简写方法语法 `shorthand method syntax`。

---

### 3. 为什么对象里不一定要用箭头函数

课程里建议：

> 当对象中定义方法时，更推荐简写方法语法，而不是箭头函数。

因为：
- 更符合对象方法的习惯
- 更易读

另外，箭头函数和普通函数在 `this` 上也有差异，不过本课没有深入展开。

---

## 二十、`addEventListener`

### 1. 基本作用

对应视频时间：`00:52:53`

它用于给元素添加事件监听。

```js
buttonElement.addEventListener('click', () => {
  console.log('clicked');
});
```

含义：
- 第一个参数：事件类型
- 第二个参数：事件发生时执行的函数

---

### 2. 为什么比 `onclick` 更好

对应视频时间：`00:56:04`

课程里给了两个关键优势：

1. 可以给同一个事件添加多个监听器
2. 可以移除监听器

所以结论是：

> 实际开发中，通常更推荐 `addEventListener`，而不是直接写 `onclick`。

---

### 3. 常见误区：不要把函数调用结果传进去

对应视频时间：`01:01:09`

错误写法：

```js
button.addEventListener('click', playGame('rock'));
```

为什么错？

因为这会立刻执行 `playGame('rock')`，然后把返回值传进去。

而 `addEventListener` 需要的是：

> 一个函数

不是函数执行后的结果。

正确写法：

```js
button.addEventListener('click', () => {
  playGame('rock');
});
```

这也是初学者最容易错的地方之一。

---

## 二十一、`removeEventListener`

### 1. 基本概念

对应视频时间：`00:56:56`

```js
buttonElement.removeEventListener('click', eventListener);
```

它可以移除之前加上的监听器。

---

### 2. 必须传入“同一个函数引用”

这是重点。

如果你这样写：

```js
buttonElement.removeEventListener('click', () => {
  console.log('clicked');
});
```

通常删不掉之前那个监听器，因为这已经是一个新的函数了。

所以要先保存：

```js
const eventListener = () => {
  console.log('clicked');
};

buttonElement.addEventListener('click', eventListener);
buttonElement.removeEventListener('click', eventListener);
```

这说明：

> 删除事件监听器时，函数引用必须完全相同。

---

## 二十二、键盘事件与事件对象 Event Object

### 1. 监听键盘事件

对应视频时间：`01:05:05`

```js
document.body.addEventListener('keydown', (event) => {
  console.log(event.key);
});
```

这里监听的是：
- `keydown`

表示键盘按下时触发。

---

### 2. 什么是事件对象

对应视频时间：`01:06:34`

事件触发时，浏览器会提供一个事件对象。

它包含很多信息，比如：
- 是什么事件
- 点击了哪个元素
- 按下了哪个键

这里通过参数接收：

```js
(event) => { ... }
```

---

### 3. `event.key`

对应视频时间：`01:06:34`

它表示用户按下的键。

例如：
- 按 `r`，`event.key === 'r'`
- 按 `p`，`event.key === 'p'`
- 按 `s`，`event.key === 's'`

然后就可以写：

```js
if (event.key === 'r') {
  playGame('rock');
}
```

---

## 二十三、`querySelectorAll()`

### 1. 为什么需要它

对应视频时间：`01:13:43`

`querySelector()` 只会返回第一个匹配元素。

但 Todo List 里的删除按钮有很多个。

所以需要：

```js
document.querySelectorAll('.js-delete-todo-button');
```

---

### 2. 它返回什么

对应视频时间：`01:14:14`

课程里说它返回“一个像数组一样的列表”。

更准确地说，它返回的是一个元素集合。

对初学者来说可以先理解成：

> 一个可遍历的元素列表。

在本课里，这个结果可以配合 `forEach` 使用。

---

### 3. 典型使用方式

```js
document
  .querySelectorAll('.js-delete-todo-button')
  .forEach((deleteButton, index) => {
    deleteButton.addEventListener('click', () => {
      todoList.splice(index, 1);
      renderTodoList();
    });
  });
```

这段代码把本课很多知识串在一起了：
- `querySelectorAll`
- `forEach`
- 箭头函数
- `addEventListener`
- 闭包

---

## 二十四、`filter()`

### 1. 基本作用

对应视频时间：`01:19:01`

`filter` 用来：

> 根据条件筛选数组中的元素，返回一个新数组。

例子：

```js
const result = [1, -3, 5].filter((value) => {
  return value >= 0;
});

console.log(result); // [1, 5]
```

---

### 2. 它是怎么工作的

对于数组中的每一项：
- 如果回调返回 `true`，保留
- 如果回调返回 `false`，丢弃

所以：

```js
value >= 0
```

本身就会返回布尔值，可以直接作为判断条件。

---

### 3. `filter` 的本质

可以理解成：

> 我给你一个标准，你帮我挑出符合标准的元素。

这是它和 `map` 的根本区别：
- `filter` 是“留下谁”
- `map` 是“把每个元素变成什么”

---

## 二十五、`map()`

### 1. 基本作用

对应视频时间：`01:22:53`

`map` 用来：

> 把一个数组转换成另一个数组。

例如：

```js
const result = [1, 1, 3].map((value) => {
  return value * 2;
});

console.log(result); // [2, 2, 6]
```

---

### 2. 它和 `filter` 的区别

`filter`：
- 决定是否保留当前元素

`map`：
- 决定当前元素要变成什么新值

对比：

```js
arr.filter(value => value >= 0)
arr.map(value => value * 2)
```

---

### 3. `map` 的直觉理解

你可以把它理解成：

> 对数组中的每个元素做一次“翻译”或“变形”。

比如：
- 数字翻倍
- 字符串转大写
- 从对象中提取某个字段

---

## 二十六、数组方法的关系梳理

这一课出现了 3 个重要数组方法：

### 1. `forEach`
- 用于遍历
- 重点是“执行动作”
- 不返回转换结果供你继续使用

### 2. `filter`
- 用于筛选
- 返回保留下来的元素组成的新数组

### 3. `map`
- 用于转换
- 返回转换后的新数组

可以这样快速区分：

- `forEach`：做事
- `filter`：挑选
- `map`：变形

---

## 二十七、闭包 Closure

### 1. 本课定义

对应视频时间：`01:26:39`

字幕中的核心意思是：

> 如果一个函数可以访问某个值，那么它会一直能访问那个值。

这就是本课对闭包的入门解释。

---

### 2. 为什么删除按钮能拿到正确的 `index`

对应视频时间：`01:27:14`

看这类代码：

```js
deleteButtons.forEach((deleteButton, index) => {
  deleteButton.addEventListener('click', () => {
    todoList.splice(index, 1);
    renderTodoList();
  });
});
```

当循环结束后，你可能会问：

> `index` 不是早就没了吗，为什么点击按钮时还能用？

答案就是闭包：
- 这个点击回调函数“记住了”当时那个 `index`
- 即使 later 再点击，它也还能访问

---

### 3. 初学者应该怎么理解闭包

先不要把它想得太玄。

你现在可以把闭包理解成：

> 函数会把它创建时周围需要用到的变量一起“带走”。

这就是为什么：
- 定时器回调能访问外层变量
- 事件监听回调能访问外层变量
- `forEach` 里的内部函数能访问 `index`

---

### 4. 闭包不是刻意制造出来的

课程里也强调了一点：

> 闭包在写 JavaScript 时会自然发生。

所以你不用一开始就专门“写闭包”，而是先学会识别：
- 这个内部函数在用外部变量
- 那这里就发生了闭包

---

## 二十八、本课隐含但非常重要的思维升级

### 1. 函数式风格开始出现

这一课虽然没有系统讲“函数式编程”，但你已经接触到它的影子了：
- 函数作为值
- 回调函数
- `forEach`
- `filter`
- `map`

这说明 JS 不只是“命令式地一步步写”，也可以通过组合函数来表达逻辑。

---

### 2. 事件驱动思维

通过 `addEventListener`，你开始接触“事件驱动”：

不是代码一开始就全部执行，
而是：
- 点击时执行
- 按键时执行
- 时间到了执行

这和前面“从上到下立即执行”的脚本思维不同，是浏览器编程的核心模式。

---

### 3. 数据与行为都可以抽象

上一课更偏“数据结构”：
- 数组
- 对象

这一课开始抽象“行为”：
- 把行为存成函数
- 把行为传来传去
- 给元素绑定行为

这会让你后面对组件、模块、框架的理解快很多。

---

## 二十九、常见错误

### 1. 把函数调用结果传给回调位置

错误：

```js
addEventListener('click', playGame('rock'));
```

正确：

```js
addEventListener('click', () => {
  playGame('rock');
});
```

---

### 2. 忘记 `setInterval` 需要保存 ID

如果不保存 ID，就没法停止它。

---

### 3. 在需要 `break` 的时候硬用 `forEach`

如果你确实要提前中断，直接换 `for` 更合理。

---

### 4. 不理解 `filter` 和 `map` 的区别

很多初学者会混淆：
- `filter` 是保留或丢弃
- `map` 是把值转换成另一个值

---

### 5. 误以为 `querySelectorAll` 返回的就是单个元素

它返回的是一组元素，不是一个元素。

---

### 6. 认为闭包是特殊语法

闭包不是单独某个关键字，而是函数和作用域共同产生的结果。

---

## 三十、本课建议掌握到什么程度

### 1. 语法层面
- 会写函数表达式
- 会写匿名函数
- 会写箭头函数
- 会用 `setTimeout`、`setInterval`、`clearInterval`
- 会用 `forEach`、`filter`、`map`
- 会写 `addEventListener`
- 会读懂 `event.key`

### 2. 思维层面
- 知道函数也是值
- 理解回调函数是什么
- 理解同步和异步的区别
- 知道什么时候适合用数组方法
- 能识别闭包场景

### 3. 项目层面
- 能给按钮绑定点击事件
- 能给键盘绑定事件
- 能把 `onclick` 改成 `addEventListener`
- 能用 `forEach` 重构列表渲染
- 能用 `filter` 和 `map` 解决简单数组题

---

## 三十一、复习版总结

这一课最核心的内容可以压缩成下面几句话：

- 函数也是值，所以函数可以存到变量里、对象里，也可以作为参数传来传去。
- 传给另一个函数的函数叫回调函数。
- `setTimeout` 在未来执行一次函数，`setInterval` 周期性执行函数。
- 定时器相关 API 是异步的，不会阻塞后续同步代码。
- `forEach` 用于遍历数组，`filter` 用于筛选数组，`map` 用于转换数组。
- 箭头函数是普通函数的简洁写法，特别适合短小回调。
- `addEventListener` 比 `onclick` 更灵活，推荐优先使用。
- `querySelectorAll` 可以获取多个元素，再配合 `forEach` 批量绑定事件。
- 事件对象里包含事件相关信息，例如 `event.key`。
- 闭包让内部函数可以持续访问外部变量。

---

## 三十二、课后练习建议

### 1. 函数基础练习
- 把一个普通函数改写成函数表达式
- 把函数表达式改写成箭头函数
- 写一个函数，接收另一个函数并调用它

### 2. 定时器练习
- 用 `setTimeout` 延迟 2 秒打印一句话
- 用 `setInterval` 每秒打印一次数字
- 5 秒后停止这个 interval

### 3. 数组方法练习
- 用 `forEach` 打印数组中的每一项
- 用 `filter` 保留所有偶数
- 用 `map` 把数组中每个数字乘以 3

### 4. 事件练习
- 给按钮添加点击事件
- 给输入框添加键盘事件
- 点击按钮后修改页面文字

### 5. 闭包理解练习
- 写一个 `forEach`，在回调里打印 `index`
- 给多个按钮绑定点击事件，点击时打印自己的索引

---

## 三十三、最后提醒

Lesson 12 是一个非常关键的过渡课。

前面你只是“会写函数”，这一课之后你应该开始理解：

- 函数可以像数据一样流动
- 浏览器里的很多功能都依赖回调
- 数组方法本质上也是在“把函数传进去”
- 事件系统和定时器系统都和函数值密切相关

如果你把这一课真正吃透，后面学习：
- 更复杂的异步
- Promise / async / await
- 更复杂的 DOM 交互
- React / Vue 里的事件和回调

都会顺很多。
