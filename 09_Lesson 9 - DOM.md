# Lesson 9 - DOM 知识点整理

这份笔记按照和前面课程相同的模式整理：先列大纲，再详细讲解每个知识点，并尽量附上对应视频时间，方便你回到原视频定位内容。主干内容来自 `09_Lesson 9 - DOM.srt`，同时补充了字幕里提到但没有完全展开、初学者应该一起掌握的相关知识点。

---

## 一、知识点大纲

### 1. 本课核心主题

1. `DOM` 是什么，为什么它很重要  
   对应视频时间：`00:00:03`、`00:05:01`
2. `document` 对象与网页的关系  
   对应视频时间：`00:03:02`
3. `document.title`、`document.body`、`innerHTML`  
   对应视频时间：`00:04:47`、`00:08:03`、`00:10:23`
4. `document.querySelector()` 获取页面元素  
   对应视频时间：`00:13:35`
5. 用 `class` 和类选择器选择特定元素  
   对应视频时间：`00:19:03`
6. 把 HTML 元素保存到变量中  
   对应视频时间：`00:21:18`
7. `innerHTML` 和 `innerText` 的区别  
   对应视频时间：`00:16:36`、`00:33:03`
8. 用 DOM 完成三个小项目  
   对应视频时间：`00:23:24`
9. 输入框的 `value` 属性  
   对应视频时间：`00:53:00`
10. `onclick`、`onkeydown` 和事件 `event`  
   对应视频时间：`01:00:58`、`01:02:10`
11. 从 DOM 读取值时的字符串类型、`Number()` 转换  
   对应视频时间：`00:58:40`、`01:00:03`
12. `String()`、类型强制补充  
   对应视频时间：`01:07:20`
13. `window` 对象  
   对应视频时间：`01:09:20`

### 2. 本课项目线索

这一课不是只讲概念，而是通过三个项目学习 DOM：

1. YouTube 订阅按钮
2. 石头剪刀布页面版
3. Amazon 运费计算器

通过这三个项目，逐步学会：

1. 获取页面元素
2. 读取元素内容
3. 修改页面内容
4. 处理按钮点击
5. 处理输入框和键盘事件

### 3. 初学者必须掌握的重点

学完这一课，至少应该掌握：

1. `DOM` 让 JavaScript 可以控制网页
2. HTML 元素进入 JavaScript 后会变成对象
3. 会用 `querySelector()` 获取元素
4. 会修改元素的 `innerHTML` / `innerText`
5. 知道输入框读值要用 `.value`
6. 知道从输入框读出来的通常是字符串
7. 会用 `Number()` 转数字
8. 能看懂 `onclick` 和 `onkeydown`
9. 会利用 `event.key` 判断按下了哪个键

---

## 二、本课整体理解

这一课是 JavaScript 初学阶段的关键转折点。

前面几课你学的大多是：

1. 值
2. 变量
3. 条件判断
4. 函数
5. 对象

而这一课开始，你学的是：

JavaScript 怎么真正操作网页。

也就是说，从这一课开始，代码不只是“在控制台里运行”，而是开始真正和页面互动了。

---

## 三、什么是 DOM

### 1. DOM 的含义

对应视频时间：`00:00:03`、`00:05:01`

`DOM` 是 `Document Object Model` 的缩写，中文常翻成“文档对象模型”。

你可以先这样理解：

1. `Document`：网页文档
2. `Object`：网页中的内容会以对象形式出现在 JavaScript 里
3. `Model`：JavaScript 用一套模型表示网页

所以 `DOM` 的本质是：

让 JavaScript 用对象的方式表示网页，并操作网页。

---

### 2. 为什么 DOM 很重要

如果没有 DOM，JavaScript 就很难直接控制页面。  
有了 DOM 之后，JavaScript 才能做这些事：

1. 改页面文字
2. 改按钮内容
3. 读取输入框内容
4. 根据用户点击更新页面

所以 DOM 是“网页交互”的核心基础。

---

## 四、`document` 对象

### 1. `document` 是什么

对应视频时间：`00:03:02`

`document` 是一个内建对象。  
它代表当前网页。

```js
document
```

这个对象和网页是连在一起的。

---

### 2. 以前其实已经见过 `document`

对应视频时间：`00:03:20`

第一课里学过：

```js
document.body.innerHTML = 'hello';
```

当时只是先用，现在这一课开始你终于能真正理解这段代码了。

---

### 3. 为什么修改 `document` 会影响网页

对应视频时间：`00:04:26`

因为 `document` 不是普通对象，它和当前网页直接绑定。  
所以你改它的某些属性时，页面也会一起变。

这正是 DOM 的核心。

---

## 五、`document.title`

### 1. 读取网页标题

对应视频时间：`00:06:54`

```js
console.log(document.title);
```

这会得到浏览器标签页顶部显示的标题。

---

### 2. 修改网页标题

对应视频时间：`00:07:20`

```js
document.title = 'Changed';
```

执行后，标签页标题会立刻变化。

这说明：

1. DOM 不只是读取网页信息
2. 还可以直接修改网页显示

---

## 六、`document.body`

### 1. `document.body` 是什么

对应视频时间：`00:08:03`

`document.body` 表示网页里的 `<body>` 元素。

```js
console.log(document.body);
```

这会把 `body` 元素放进 JavaScript 里。

---

### 2. HTML 元素进入 JavaScript 后会变成对象

对应视频时间：`00:09:52`

课程里强调了一点：

当 HTML 元素进入 JavaScript 后，它会变成一个 JavaScript 对象。

这意味着：

1. 它有属性
2. 它有方法
3. 可以保存到变量里

所以你后面看到的“元素操作”，本质上都是在操作对象。

---

## 七、`innerHTML`

### 1. `innerHTML` 是什么

对应视频时间：`00:10:23`

`innerHTML` 表示一个元素内部的 HTML 内容。

例如：

```js
document.body.innerHTML
```

这会得到 `<body>` 里面所有 HTML。

---

### 2. 读取 `innerHTML`

对应视频时间：`00:10:45`

```js
console.log(document.body.innerHTML);
```

可以把元素内部的 HTML 读出来。

---

### 3. 修改 `innerHTML`

对应视频时间：`00:11:08`

```js
document.body.innerHTML = 'changed';
```

这会直接替换掉页面中 `body` 内的所有 HTML。

所以要注意：

1. 它不是“追加”
2. 而是“整体替换”

---

### 4. `innerHTML` 可以放 HTML 代码，不只是纯文本

对应视频时间：`00:12:18`

```js
document.body.innerHTML = '<button>Good Job</button>';
```

执行后，页面上会真正出现一个按钮。

这说明：

JavaScript 可以通过修改 `innerHTML` 动态生成 HTML。

---

### 5. `innerHTML` 的典型用途

初学阶段最常见的用途是：

1. 在页面上输出计算结果
2. 动态更新某一块内容
3. 根据变量生成 HTML

不过它也有一个特点：  
如果你频繁整块替换，会把原先那一块内容整个换掉。

---

## 八、`document.querySelector()`

### 1. 为什么需要 `querySelector()`

对应视频时间：`00:13:35`

`document.body` 只能直接拿到 `body` 元素。  
但网页上通常有很多不同元素。

这时就需要：

```js
document.querySelector()
```

它可以让我们从页面中选择任意元素。

---

### 2. 基本语法

对应视频时间：`00:14:10`

```js
document.querySelector('button');
```

这会获取页面上的第一个 `button` 元素。

---

### 3. 返回值是什么

对应视频时间：`00:14:56`

返回值是一个 HTML 元素对象。  
也就是说，它会把页面中的元素放进 JavaScript。

你可以继续对它读写属性：

```js
document.querySelector('button').innerHTML = 'Changed';
```

---

### 4. `querySelector()` 默认只拿第一个匹配元素

对应视频时间：`00:18:40`

如果页面上有多个按钮：

```js
document.querySelector('button');
```

默认只会选中第一个。

这一点很关键，后面经常影响调试。

---

## 九、类选择器和 `class`

### 1. 为什么要用 `class`

对应视频时间：`00:19:03`

如果页面上有多个同类元素，比如两个按钮，只写：

```js
document.querySelector('button');
```

不够精确。

这时就要给特定元素加 `class`：

```html
<button class="js-button">Second button</button>
```

---

### 2. 用类选择器获取元素

对应视频时间：`00:19:45`

```js
document.querySelector('.js-button');
```

注意前面有一个点 `.`，表示按 class 选择。

---

### 3. 为什么课程里常用 `js-` 前缀

对应视频时间：`00:20:50`

课程里专门说了，常见做法是把给 JavaScript 用的类名写成：

1. `js-button`
2. `js-subscribe-button`
3. `js-score`

这样一眼就知道这个类主要是给 JavaScript 用的，而不是专门为 CSS 样式服务。

这是个很实用的工程习惯。

---

## 十、把元素保存到变量

### 1. 为什么要保存到变量

对应视频时间：`00:21:18`

如果一个元素要用很多次，每次都重新写一长串：

```js
document.querySelector('.js-button')
```

会很重复。

更好的写法是：

```js
const buttonElement = document.querySelector('.js-button');
```

---

### 2. 命名习惯

对应视频时间：`00:21:40`

课程里推荐变量名后面加上 `Element`，比如：

1. `buttonElement`
2. `inputElement`

这样看到变量名时，就知道它保存的是 HTML 元素对象。

---

## 十一、`innerHTML` 和 `innerText`

### 1. `innerHTML`

对应视频时间：`00:16:36`

它读取或修改的是“元素内部的 HTML”。

所以：

1. 会包含 HTML 结构
2. 可能受空格、换行影响
3. 可以插入 HTML 标签

---

### 2. `innerText`

对应视频时间：`00:33:03`

在订阅按钮项目里，课程发现 `innerHTML` 受到空格和换行影响。  
所以改用：

```js
buttonElement.innerText
```

`innerText` 更适合只处理纯文本内容。

---

### 3. 什么时候优先用哪一个

对初学者最实用的经验是：

1. 只想处理文字：优先考虑 `innerText`
2. 想插入或读取 HTML 结构：用 `innerHTML`

---

## 十二、项目一：YouTube 订阅按钮

### 1. 项目目标

对应视频时间：`00:26:50`

点击按钮时：

1. 如果当前是 `Subscribe`
2. 就改成 `Subscribed`
3. 再点一次又切回去

---

### 2. 这类交互的基本算法

对应视频时间：`00:27:12`

课程里先用自然语言写步骤：

1. 点击按钮
2. 检查按钮当前文字
3. 如果是 `Subscribe`，改成 `Subscribed`
4. 否则改回 `Subscribe`

这就是“先想步骤，再写代码”的算法思维。

---

### 3. 核心实现思路

对应视频时间：`00:29:40` 到 `00:31:40`

核心代码逻辑大致是：

```js
const buttonElement = document.querySelector('.js-subscribe-button');

if (buttonElement.innerText === 'Subscribe') {
  buttonElement.innerText = 'Subscribed';
} else {
  buttonElement.innerText = 'Subscribe';
}
```

---

### 4. 为什么空格会导致判断失败

对应视频时间：`00:32:10`

如果 HTML 写成：

```html
<button>
  Subscribe
</button>
```

里面可能会带上换行和空格。  
这时 `innerHTML` 得到的就不再是精确的 `'Subscribe'`。

所以课程改用 `innerText` 来避免这个问题。

---

### 5. 把 `onclick` 中的代码挪到函数里

对应视频时间：`00:33:40` 到 `00:35:00`

课程里进一步把按钮里的 JavaScript 提取成函数：

```js
function subscribe() {
  // ...
}
```

然后在 `onclick` 中只写：

```html
onclick="subscribe()"
```

这样做的好处：

1. HTML 更干净
2. JavaScript 更集中
3. 更容易维护

---

## 十三、项目二：石头剪刀布页面版

### 1. 项目升级目标

对应视频时间：`00:35:20`

和之前版本相比，这次不是用弹窗显示结果，而是：

1. 在页面上显示结果
2. 在页面上显示玩家和电脑的出拳
3. 在页面上显示并更新分数

---

### 2. 先准备专门显示内容的元素

对应视频时间：`00:37:12`、`00:44:20`

课程里先在 HTML 中加了几个段落：

1. `js-score`
2. `js-result`
3. `js-moves`

它们的作用就是当作“占位位置”，后面由 JavaScript 把内容填进去。

---

### 3. 把分数显示到页面上

对应视频时间：`00:38:15`

做法是：

1. 用 `querySelector('.js-score')` 拿到元素
2. 给它的 `innerHTML` 赋值
3. 用模板字符串插入 `wins`、`losses`、`ties`

---

### 4. 为什么段落会把后面的按钮挤到下一行

对应视频时间：`00:39:40`

课程里顺便补充了 HTML/CSS 知识：

`<p>` 是块级元素 `block element`。  
块级元素会自己占据整行，所以后面的按钮会被挤到下面。

这不是 JavaScript 问题，而是 HTML 布局规则。

---

### 5. 更新页面时也要同步更新 DOM

对应视频时间：`00:41:00`

只改数据不够，页面不会自动变。  
所以每次分数变化后，还要再执行一次更新页面的代码。

这是前端里非常重要的思维：

1. 改数据
2. 再更新界面

---

### 6. 提取 `updateScoreElement()` 函数

对应视频时间：`00:42:12`

因为“更新页面上的分数”这段代码会重复出现，所以课程把它提取成函数：

```js
function updateScoreElement() {
  // 更新页面中的分数字符串
}
```

然后：

1. 页面加载时调用一次
2. 每局游戏结束后调用一次
3. 重置分数后也调用一次

这就是函数复用的实际应用。

---

### 7. 显示结果和双方出拳

对应视频时间：`00:45:15` 到 `00:47:00`

课程里分别更新了：

1. `.js-result`
2. `.js-moves`

其中 `.js-moves` 用模板字符串把 `playerMove` 和 `computerMove` 插进去。

这样页面就能完整显示一局游戏的信息。

---

### 8. 删除弹窗

对应视频时间：`00:47:15`

当页面已经能显示结果后，原来的 `alert(...)` 就不需要了，可以删除。

这说明：

1. 以前用弹窗只是为了先实现功能
2. 现在学了 DOM，就可以把结果真正显示到页面上

---

## 十四、项目三：Amazon 运费计算器

### 1. 项目目标

对应视频时间：`00:48:00`

这个项目的规则是：

1. 输入订单金额
2. 小于 `$40`，加 `$10` 运费
3. 大于等于 `$40`，免运费
4. 在页面上显示总价

---

### 2. 输入框元素 `<input>`

对应视频时间：`00:49:30`

课程里创建了输入框：

```html
<input>
```

并说明它是一个 `void element`，也就是不需要结束标签的元素。

---

### 3. `placeholder` 属性

对应视频时间：`00:50:10`

输入框中的灰色提示文字来自：

```html
placeholder="Cost of order"
```

它只是在输入框为空时显示的提示，不是真正输入的值。

---

### 4. 用 `.value` 读取输入框内容

对应视频时间：`00:53:00`

输入框和普通按钮不同，它没有内部 HTML。  
所以读取输入框内容时不能用 `innerHTML`，而要用：

```js
inputElement.value
```

这点非常重要。

---

### 5. 显示总价

对应视频时间：`00:56:16`

课程里先准备了一个段落 `.js-total-cost`，然后用：

```js
document.querySelector('.js-total-cost').innerHTML = `$${cost}`;
```

把结果显示到页面上。

---

## 十五、从 DOM 读出来的值通常是字符串

### 1. 问题出现在哪

对应视频时间：`00:57:00` 到 `00:58:20`

课程里输入 `25` 后，本来预期结果是 `35`，但却出现了类似 `2510` 这种错误结果。

原因是：

从输入框读出来的 `value` 是字符串，不是数字。

---

### 2. 为什么会拼接而不是加法

对应视频时间：`00:58:40`

如果：

```js
let cost = '25';
cost = cost + 10;
```

那 JavaScript 会把 `10` 也转成字符串，然后拼接成：

```js
'2510'
```

这就是类型强制 `type coercion`。

---

### 3. 用 `Number()` 转成数字

对应视频时间：`00:59:40`

正确写法是：

```js
let cost = Number(inputElement.value);
```

这样才可以正常做数学运算。

---

### 4. 最实用的经验

只要你是从 DOM 的输入框拿值：

1. 先默认它是字符串
2. 如果要做数学运算，记得手动转数字

这是前端初学者非常容易踩坑的一点。

---

## 十六、`onclick`、`onkeydown` 和事件

### 1. `onclick`

这一课前半段一直在用：

```html
onclick="someFunction()"
```

它表示：点击元素时，运行一段 JavaScript。

---

### 2. `onkeydown`

对应视频时间：`01:00:58`

课程后面又讲了：

```html
onkeydown="..."
```

它表示：当用户在输入框中按下键盘某个键时，运行 JavaScript。

---

### 3. 什么是事件 `event`

对应视频时间：`01:01:45`、`01:02:10`

点击、按键这些都叫事件。  
而浏览器会把事件相关信息放进一个特殊对象里，叫：

```js
event
```

这个对象里包含了很多信息，比如按下的是哪个键。

---

### 4. `event.key`

对应视频时间：`01:03:10`

```js
event.key
```

可以得到当前按下的键。

例如按回车时，通常会得到：

```js
'Enter'
```

---

### 5. 用回车键触发计算

对应视频时间：`01:04:00`

课程里的逻辑大致是：

```js
if (event.key === 'Enter') {
  calculateTotal();
}
```

这样用户按回车，就能达到和点击“Calculate”按钮一样的效果。

---

### 6. 事件对象传进函数

对应视频时间：`01:05:50`

课程最后把按键处理逻辑提取成函数，例如：

```js
function handleCostKeydown(event) {
  if (event.key === 'Enter') {
    calculateTotal();
  }
}
```

这里 `event` 是函数参数。  
调用时，需要把事件对象传进去。

这再次体现了“参数把值传进函数”的知识。

---

## 十七、`String()` 与类型强制补充

### 1. `String()` 函数

对应视频时间：`01:07:20`

除了 `Number()` 可以把字符串转数字，`String()` 也可以把值转字符串：

```js
String(25); // '25'
```

---

### 2. 为什么不要依赖隐式类型转换做数学

对应视频时间：`01:08:00`

课程举了两个例子：

1. `'25' - 5` 可能得到 `20`
2. `'25' + 5` 却得到 `'255'`

这说明 JavaScript 的自动类型转换规则并不统一。

所以更好的习惯是：

1. 做数学时确保自己手里的就是数字
2. 不要靠隐式转换碰运气

---

## 十八、`window` 对象

### 1. `window` 是什么

对应视频时间：`01:09:20`

课程最后介绍了另一个内建对象：

```js
window
```

它代表浏览器窗口。

如果说：

1. `document` 代表网页

那么：

1. `window` 更像代表浏览器环境

---

### 2. `document` 在 `window` 里面

对应视频时间：`01:10:00`

```js
window.document
```

和：

```js
document
```

本质上指的是同一个东西。

---

### 3. `console` 和 `alert` 也在 `window` 里面

对应视频时间：`01:10:30`

例如：

```js
window.console.log('hello');
window.alert('hello');
```

也能工作。

---

### 4. 为什么平时不写 `window.`

对应视频时间：`01:11:15`

因为很多情况下，JavaScript 会自动帮你补上 `window.`。  
所以平时直接写：

1. `document`
2. `console.log(...)`
3. `alert(...)`

就够了。

但理解它们背后属于 `window`，有助于你建立更完整的认识。

---

## 十九、本课应该顺手补充理解的内容

### 1. DOM 是 JavaScript 和 HTML 的桥梁

这句话非常值得记住。  
没有 DOM，JavaScript 很难真正操作网页内容。

---

### 2. 页面上的“显示结果”通常都要先准备一个容器元素

比如：

1. 一个段落 `<p>`
2. 一个 `<div>`
3. 一个按钮

然后再用 JavaScript 把内容塞进去。

这是一种很常见的页面开发模式。

---

### 3. 前端里的很多交互都可以归纳成同一套路

1. 监听事件
2. 获取数据
3. 计算新结果
4. 更新 DOM

这一课的三个项目，本质上都在练这套流程。

---

## 二十、常见错误与易混点

### 1. 把 `querySelector()` 当成会返回所有元素

不是。  
`querySelector()` 默认只返回第一个匹配元素。

---

### 2. 输入框使用 `innerHTML` 读取内容

输入框读值要用：

```js
inputElement.value
```

而不是：

```js
inputElement.innerHTML
```

---

### 3. 忘记类选择器前面加 `.`

错误：

```js
document.querySelector('js-button')
```

正确：

```js
document.querySelector('.js-button')
```

---

### 4. 从输入框拿值后直接做加法

```js
let cost = inputElement.value;
cost = cost + 10;
```

这通常会变成字符串拼接。  
应该先转数字：

```js
let cost = Number(inputElement.value);
```

---

### 5. 用 `innerHTML` 比较按钮文字时没注意空格

如果按钮内容在 HTML 中带换行和缩进，`innerHTML` 很可能不是你以为的精确文本。  
这时更适合用 `innerText`。

---

### 6. 更新了数据，却没更新页面

这在石头剪刀布项目里很常见。  
修改 `score` 后，如果不再执行一次更新 DOM 的代码，页面不会自动变化。

---

## 二十一、本课最重要的结论

这一课最应该牢固掌握的是：

1. `DOM` 让 JavaScript 可以直接控制网页
2. `document` 代表网页
3. `querySelector()` 可以从页面中获取元素
4. HTML 元素进入 JavaScript 后会变成对象
5. `innerHTML` / `innerText` 可以修改元素显示内容
6. 输入框要用 `.value`
7. 从输入框得到的通常是字符串
8. 需要数学运算时要用 `Number()`
9. 点击和按键都是事件
10. `event.key` 可以帮助判断键盘输入

---

## 二十二、建议复习顺序

如果你准备回看这一课，建议按这个顺序：

1. 先理解 `DOM` 和 `document`
2. 再理解 `title`、`body`、`innerHTML`
3. 再练 `querySelector()`
4. 再练 `class` 选择器和保存元素变量
5. 再看订阅按钮项目
6. 再看石头剪刀布页面版
7. 最后看输入框项目、类型转换、键盘事件和 `window`

这样能把概念和项目串起来。

---

## 二十三、练习建议

### 1. 基础 DOM 练习

1. 用 JavaScript 读取 `document.title`
2. 修改 `document.title`
3. 用 `document.body.innerHTML` 替换页面内容

### 2. 元素选择练习

1. 页面上放两个按钮
2. 用 `querySelector('button')` 获取第一个
3. 给第二个按钮加 class
4. 用 `.className` 选择第二个按钮

### 3. 文本修改练习

1. 创建一个按钮
2. 点击后把文字改成别的
3. 再点击恢复原文字

### 4. 输入框练习

1. 创建一个输入框和按钮
2. 点击按钮后读取输入框内容
3. 把输入内容显示到页面上
4. 尝试用回车键也触发相同逻辑

### 5. 类型转换练习

1. 从输入框输入 `25`
2. 直接加 `10`，观察问题
3. 再用 `Number()` 修复

---

## 二十四、你学完这课后应该具备的能力

学完这一课后，你应该开始具备这些能力：

1. 能让按钮、输入框和页面互动起来
2. 能从页面读取用户输入
3. 能把计算结果渲染回页面
4. 能写出最基础的交互式网页功能

如果这一课没有吃透，后面学数组渲染、Todo List、模块化页面、测试 DOM 都会明显变难。  
所以 `lesson 9` 是非常值得反复回看的关键课。

