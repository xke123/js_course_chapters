# Lesson 18 - Backend Async Await 知识点整理

这份笔记基于 `18_Lesson 18 - Backend Async Await.srt` 整理，并补充了初学者学习这一课时应该一起掌握的相关知识点。`lesson 18` 的主线有六条：

1. 理解什么是前端、后端和 HTTP 请求
2. 学会使用 `XMLHttpRequest` 和 `fetch` 与后端通信
3. 理解异步代码、回调函数、Promise 和 `async/await`
4. 学会处理网络请求中的成功与失败
5. 学会在项目里创建订单、跳转页面和读取 URL 参数
6. 建立“前端通过 API 和后端交换数据”的整体思维

---

## 一、知识点大纲

### 1. 本课核心主题
- 什么是后端 `backend`：`00:00:04`
- 前端 `frontend` 和后端的分工：`00:01:00`
- 什么是 HTTP 消息：`00:01:32`
- 新建 `backend-practice.js`：`00:02:02`
- 内置类 `XMLHttpRequest`：`00:02:29`
- `xhr.open('GET', url)`：`00:03:25`
- URL、域名 `domain name`、`https`：`00:04:24`
- `xhr.send()` 发送请求：`00:06:45`
- 在 Network 面板查看请求：`00:08:20`
- 请求 `request` 与响应 `response`：`00:11:47`
- 响应是异步的：`00:12:35`
- `load` 事件：`00:14:05`
- URL 路径 `path`：`00:16:20`
- 不支持的路径与错误信息：`00:18:20`
- 状态码 `status code`：`00:19:18`
- 后端文档与 API：`00:21:40`
- 不同响应类型：文本、JSON、HTML、图片：`00:23:00`
- 异步测试和 Jasmine 的 `done`：`00:57:01`
- Promise 基础：`00:58:02`
- `new Promise()` 和 `resolve()`：`00:58:58`
- `.then()`：`01:02:15`
- 回调嵌套问题：`01:06:25`
- `Promise.all()`：`01:19:10`
- `fetch()`：`01:25:30`
- `response.json()`：`01:29:10`
- 让函数返回 Promise：`01:33:40`
- 把项目代码改成 `fetch`：`01:35:45`
- `async/await`：`01:39:53`
- `async` 会让函数返回 Promise：`01:40:50`
- `await` 等待 Promise 完成：`01:43:45`
- `await` 只能在 `async` 函数里用：`01:46:00`
- `await` 的结果值：`01:50:00`
- 错误处理总览：`01:52:14`
- XHR 的错误处理：`01:53:00`
- Promise 的 `.catch()`：`01:56:00`
- `async/await` 的 `try/catch`：`01:58:20`
- 创建订单并保存：`02:21:00`
- `window.location.href` 页面跳转：`02:27:00`
- URL 参数 `query params`：`02:30:45`
- `new URL(window.location.href)`：`02:33:00`
- `searchParams.get()`：`02:34:00`
- 多个参数用 `&`：`02:36:00`
- 用 URL 参数构建 tracking 页面：`02:38:40`
- 本课总结：`02:40:34`

### 2. 本课项目线索
- 先理解浏览器如何向后端发送请求并拿到响应
- 再用 `XMLHttpRequest` 完成最基础的网络通信
- 然后理解“为什么响应拿不到”和“为什么要等待”
- 接着把回调写法升级成 Promise
- 再把 Promise 写法升级成 `fetch`
- 最后用 `async/await` 重构项目里的商品加载、购物车加载和订单创建
- 在订单页与 tracking 页之间，通过 URL 参数传递 `orderId` 和 `productId`

### 3. 初学者必须掌握的重点
- 后端本质上也是另一台计算机，负责管理数据并返回结果
- HTTP 请求不是“直接调用函数”，而是浏览器和服务器之间发消息
- 网络请求是异步的，所以不能把结果当同步值立即使用
- 回调、Promise、`async/await` 都是在解决“异步结果什么时候可用”
- `fetch()` 默认发送 `GET` 请求，并返回一个 Promise
- `response.json()` 也会返回 Promise，不是立即得到对象
- 错误处理必须区分“请求成功但业务失败”和“请求本身失败”
- URL 参数是页面间传递少量信息的常用方式

---

## 二、本课整体理解

Lesson 18 是这门课程从“纯前端练习”正式过渡到“前后端协作”的一课。

前面你写的大部分代码，都运行在浏览器里。浏览器可以：
- 渲染页面
- 响应点击
- 读取本地存储

但它本身并不适合长期保存复杂数据，也不能替代真正的服务器。

这一课开始，你会看到一个更真实的 Web 应用结构：

- 前端负责界面和交互
- 后端负责数据和业务处理
- 两者通过 HTTP 请求和响应进行通信

这一课真正的难点不是 API 语法，而是“异步思维”。  
也就是你要开始接受一个事实：

> 很多值不是马上就有，而是过一会儿才会回来。

所以本课实际上在同时训练两件事：
- 网络通信的基础认知
- JavaScript 异步编程能力

---

## 三、什么是后端 Backend

### 1. 后端的定义

对应视频时间：`00:00:04`

课程里的核心解释是：

> 后端就是另一台负责管理数据的计算机。

这句话非常重要，因为它帮你建立了正确模型：
- 你正在用的浏览器在你的电脑上运行
- 后端通常运行在另一台远程服务器上
- 你想拿商品数据、创建订单，本质上都要去“问后端”

---

### 2. 前端和后端的分工

对应视频时间：`00:01:00`

可以这样理解：

- 前端 `frontend`：用户直接看到和操作的部分
- 后端 `backend`：负责数据、数据库、订单、账户、接口等

在这个 Amazon 项目里：
- 商品列表最终来自后端
- 创建订单也交给后端
- 前端的工作是把数据展示出来，并把用户操作转换成请求

补充理解：

前端和后端不是谁更“高级”，而是分工不同。  
前端更关注：
- 用户体验
- DOM 和页面渲染
- 交互流程

后端更关注：
- 数据存储
- 权限
- 接口设计
- 业务规则

---

## 四、什么是 HTTP 请求和响应

### 1. HTTP 是浏览器和服务器交流的方式

对应视频时间：`00:01:32`

HTTP 可以理解成一种消息规则。

浏览器给服务器发一条消息：
- 我要什么资源
- 用什么方法请求
- 还可能带哪些数据

服务器收到后，再返回一条消息：
- 请求是否成功
- 返回什么数据
- 数据是什么类型

这就是一次请求响应流程。

---

### 2. 请求和响应的基本术语

对应视频时间：`00:11:47`

- `request`：请求
- `response`：响应

你可以把它想象成：

1. 浏览器发问
2. 服务器处理
3. 服务器回答

---

### 3. 请求不是瞬间完成的

对应视频时间：`00:12:35`

因为请求要经过网络，所以：
- 发送需要时间
- 服务器处理需要时间
- 响应返回也需要时间

这就是为什么网络代码通常是异步的。

这也是初学者最容易犯错的地方：

```js
const xhr = new XMLHttpRequest();
xhr.open('GET', 'https://supersimplebackend.dev');
xhr.send();

console.log(xhr.response); // 通常此时还拿不到真正数据
```

原因不是代码写错，而是响应还没回来。

---

## 五、`XMLHttpRequest` 基础

### 1. `XMLHttpRequest` 是浏览器内置类

对应视频时间：`00:02:29`

创建方式：

```js
const xhr = new XMLHttpRequest();
```

它的作用是：
- 发送 HTTP 请求
- 接收服务器响应

虽然现代开发更常用 `fetch()`，但理解 XHR 很有价值，因为它能帮助你看清底层流程。

---

### 2. `open()` 用来配置请求

对应视频时间：`00:03:25`

```js
xhr.open('GET', 'https://supersimplebackend.dev');
```

这里至少有两个关键部分：
- 请求方法：`GET`
- 请求地址：URL

补充说明：

`GET` 一般表示“读取数据”。  
这节课里最常用的是：
- 读取商品数据
- 读取购物车数据

而创建订单这种操作，通常会用 `POST`，因为它会改变服务器上的数据。

---

### 3. URL、域名、协议、路径

对应视频时间：`00:04:24`

一个 URL 常见结构可以拆成：

```txt
https://supersimplebackend.dev/hello
```

拆分后：
- `https`：协议 `protocol`
- `supersimplebackend.dev`：域名 `domain name`
- `/hello`：路径 `path`

路径的作用是告诉服务器：
- 你想访问哪个资源
- 你想调用哪个接口

例如：
- `/hello`
- `/products`
- `/orders`

不同路径通常代表不同功能。

---

### 4. `send()` 才真正发出请求

对应视频时间：`00:06:45`

```js
xhr.send();
```

`open()` 只是先准备好。  
`send()` 执行后，请求才会真的发出去。

这也是一个常见误区：
- `open()` 不等于已经请求了
- `send()` 才是触发点

---

## 六、用开发者工具查看请求

### 1. Network 面板的作用

对应视频时间：`00:08:20`

浏览器开发者工具里的 Network 面板可以帮你看到：
- 发了哪些请求
- 请求地址是什么
- 状态码是什么
- 响应内容是什么

这是学习后端交互时最重要的调试工具之一。

---

### 2. 为什么打开 Network 后要刷新页面

对应视频时间：`00:09:00` 左右

因为 Network 面板只会记录“打开之后发生的请求”。  
如果请求已经发完了，你再打开面板，通常看不到之前那次请求，所以需要刷新。

---

### 3. 调试网络问题时应该先看什么

补充知识点。

遇到“页面没数据显示”时，优先检查：

1. 请求有没有发出去
2. 请求地址对不对
3. 状态码是不是成功
4. 响应内容是不是你预期的数据
5. 前端是不是把响应解析错了

这比盲目改代码更有效。

---

## 七、路径 Path、API 和状态码

### 1. 不同路径对应不同资源

对应视频时间：`00:16:20`

同一个域名下，不同路径通常代表不同接口。

例如：
- `/hello`
- `/products/first`
- `/products`

这说明后端不是只提供一个入口，而是根据路径处理不同请求。

---

### 2. 什么是 API

对应视频时间：`00:21:40`

API 可以理解成：

> 后端提供给前端使用的一组规则和入口。

前端要知道：
- 请求发到哪里
- 用什么方法
- 会返回什么格式
- 出错时会怎样

通常这些信息会写在 API 文档里。

这也是为什么课程里强调查看后端文档。

---

### 3. 状态码表示请求结果

对应视频时间：`00:19:18`

课程里提到的重点分类：

- `2xx`：成功
- `4xx`：客户端问题
- `5xx`：服务器问题

可以这样理解：

- `2xx`：你发对了，服务器也处理成功了
- `4xx`：通常是你请求写错了，比如路径不对、参数有问题
- `5xx`：请求可能没问题，但服务器自己出错了

补充一个很常用的思维：

> 不是所有“页面报错”都是前端 bug。  
> 有时候是请求失败了，有时候是服务器本身挂了。

---

## 八、响应数据类型与 JSON

### 1. 响应可以是很多类型

对应视频时间：`00:23:00`

课程展示了多种响应类型：
- 纯文本
- JSON
- HTML
- 图片

这说明 HTTP 返回的不是“只能返回对象”，而是可以返回各种资源。

---

### 2. 为什么前端项目里 JSON 最常见

补充知识点。

因为 JSON 很适合表示结构化数据，比如：

```json
{
  "id": "abc",
  "name": "basketball",
  "priceCents": 2095
}
```

前端拿到 JSON 后，可以：
- 渲染页面
- 计算价格
- 生成订单

JSON 本质上是“字符串格式的数据表示法”，不是 JavaScript 对象本身。  
所以很多时候你还需要“解析”它。

---

## 九、XHR 的异步处理方式

### 1. `load` 事件表示响应已经到达

对应视频时间：`00:14:05`

```js
const xhr = new XMLHttpRequest();

xhr.addEventListener('load', () => {
  console.log(xhr.response);
});

xhr.open('GET', 'https://supersimplebackend.dev/hello');
xhr.send();
```

这里的关键是：
- 先注册 `load` 事件
- 等请求完成后，这个回调才会执行

也就是说：

> 你不是“立刻拿结果”，而是“结果来了再执行后续代码”。

---

### 2. 回调函数在异步代码里的意义

补充知识点。

回调函数 `callback` 的本质是：

> 先把一段将来要执行的代码保存起来，等某个时机到了再调用。

在 XHR 里，这个“某个时机”就是：
- 请求完成
- 响应返回

所以异步代码几乎总会和回调打交道。

---

## 十、异步测试与 Jasmine 的 `done`

### 1. 为什么异步代码的测试不能直接写同步断言

对应视频时间：`00:57:01`

如果你的函数内部有异步请求，那么测试代码也必须“等它完成”。

错误思路：

```js
it('loads data', function () {
  loadProducts();
  expect(products.length).toBeGreaterThan(0);
});
```

问题在于：
- `loadProducts()` 可能还没完成
- 断言就已经执行了

---

### 2. `done` 的作用

对应视频时间：`00:57:01`

Jasmine 里的 `done` 可以告诉测试框架：

> 这个测试要等我手动通知“结束”。

典型模式：

```js
it('loads data', function (done) {
  loadProducts(() => {
    expect(products.length).toBeGreaterThan(0);
    done();
  });
});
```

这里的核心思想和异步编程完全一致：
- 不要抢跑
- 结果到了再继续

---

## 十一、Promise 基础

### 1. Promise 是什么

对应视频时间：`00:58:02`

Promise 可以理解成：

> 一个代表“未来会完成的结果”的对象。

它不是最终结果本身，而是“结果的占位符”。

你现在先拿到 Promise，真正的数据将来才会到。

---

### 2. 创建 Promise

对应视频时间：`00:58:58`

```js
const promise = new Promise((resolve) => {
  resolve('finished');
});
```

这里：
- `new Promise(...)` 创建一个 Promise
- `resolve(...)` 表示“成功完成”

课程里把 `resolve` 和 Jasmine 的 `done` 做类比，这个类比对初学者很有帮助：
- `done()`：通知测试结束
- `resolve()`：通知 Promise 成功完成

---

### 3. `.then()` 用来接收成功结果

对应视频时间：`01:02:15`

```js
promise.then((value) => {
  console.log(value);
});
```

`.then()` 的意思是：

> 等这个 Promise 完成之后，再执行这里的代码。

如果 `resolve('finished')`，那么 `.then(value => ...)` 里的 `value` 就是 `'finished'`。

---

### 4. Promise 的价值

补充知识点。

Promise 解决的是“回调不好管理”的问题。  
它让异步代码：
- 更线性
- 更容易组合
- 更容易做统一错误处理

这也是后面 `fetch` 和 `async/await` 的基础。

---

## 十二、从回调到 Promise

### 1. 回调地狱的根源

对应视频时间：`01:06:25`

如果你要连续做几件异步事情，例如：

1. 先加载商品
2. 再加载购物车
3. 最后再渲染页面

使用纯回调时，代码很容易变成嵌套：

```js
loadProducts(() => {
  loadCart(() => {
    renderPage();
  });
});
```

嵌套一深：
- 可读性下降
- 错误处理分散
- 调试困难

---

### 2. 用 Promise 改写的好处

对应视频时间：`01:08:00` 到 `01:19:10` 这一段

Promise 可以把“完成后再继续”的逻辑改写成链式结构：

```js
loadProductsPromise()
  .then(() => {
    return loadCartPromise();
  })
  .then(() => {
    renderPage();
  });
```

这样代码会更接近“从上到下执行”的阅读方式。

---

### 3. `Promise.all()`

对应视频时间：`01:19:10`

如果两个异步任务可以并行执行，就不需要一个等另一个。

```js
Promise.all([
  loadProductsFetch(),
  loadCartFetch()
]).then(() => {
  renderPage();
});
```

`Promise.all()` 的含义是：

> 等数组里的所有 Promise 都完成，再继续。

这在项目里很常见，因为：
- 商品数据和购物车数据通常互不依赖
- 可以同时请求，减少等待时间

补充注意：

只要其中一个 Promise 失败，`Promise.all()` 通常就会整体失败。

---

## 十三、`fetch()` 基础

### 1. `fetch` 是更现代的请求方式

对应视频时间：`01:25:30`

```js
fetch('https://supersimplebackend.dev/products');
```

课程里把它作为比 XHR 更好的现代写法。

它的优点是：
- 语法更简洁
- 和 Promise 原生结合
- 更容易与 `async/await` 配合

---

### 2. `fetch()` 默认发送 `GET`

补充知识点。

如果你只传 URL：

```js
fetch(url);
```

默认就是 `GET` 请求，也就是“读取数据”。

如果以后要发送 `POST`、`PUT`、`DELETE`，通常需要传第二个配置对象。

---

### 3. `fetch()` 返回的是 Promise

对应视频时间：`01:28:40`

```js
fetch(url).then((response) => {
  console.log(response);
});
```

这说明：
- `fetch` 不会立刻给你最终数据
- 它先返回一个 Promise
- Promise 完成后，你会拿到 `response` 对象

---

### 4. `response.json()` 也返回 Promise

对应视频时间：`01:29:10`

```js
fetch(url)
  .then((response) => {
    return response.json();
  })
  .then((data) => {
    console.log(data);
  });
```

这里很多初学者第一次会卡住：

> 为什么我都拿到 `response` 了，`json()` 还要再等一次？

原因是：
- `response` 只是响应对象
- 把响应体解析成 JSON 也需要一步异步过程

所以 `response.json()` 返回的仍然是 Promise。

---

### 5. 让函数直接返回 Promise

对应视频时间：`01:33:40`

这是很重要的封装思路。

例如：

```js
function loadProductsFetch() {
  return fetch('https://supersimplebackend.dev/products')
    .then((response) => {
      return response.json();
    });
}
```

这样外部就可以继续链式调用：

```js
loadProductsFetch().then((products) => {
  console.log(products);
});
```

这比“把所有逻辑都写死在函数内部”更灵活。

---

## 十四、`async/await`

### 1. `async/await` 是 Promise 的更简洁写法

对应视频时间：`01:39:53`

课程里的核心观点可以概括成：

> `async/await` 是 Promise 的语法糖。

也就是说：
- 底层仍然是 Promise
- 只是写起来更接近同步代码

---

### 2. `async` 会让函数返回 Promise

对应视频时间：`01:40:50`

```js
async function example() {
  return 'hello';
}
```

虽然你写的是 `return 'hello'`，但外部接收到的其实是：

```js
Promise.resolve('hello')
```

所以：

```js
example().then((value) => {
  console.log(value); // hello
});
```

---

### 3. `await` 用来等待 Promise 完成

对应视频时间：`01:43:45`

```js
async function loadProducts() {
  const response = await fetch('https://supersimplebackend.dev/products');
  const products = await response.json();
  console.log(products);
}
```

你可以这样理解：

> `await` 会暂停当前 `async` 函数的后续执行，直到 Promise 完成。

它不会阻塞整个浏览器，只是让当前函数在这里“等一下”。

---

### 4. `await` 只能写在 `async` 函数里

对应视频时间：`01:46:00`

这是语法规则，也是高频错误。

错误示例：

```js
function test() {
  const response = await fetch(url);
}
```

正确示例：

```js
async function test() {
  const response = await fetch(url);
}
```

如果有多层函数，要注意“离 `await` 最近的那层函数”必须是 `async`。

---

### 5. `await` 的结果可以直接赋值

对应视频时间：`01:50:00`

```js
const response = await fetch(url);
const data = await response.json();
```

这里：
- `response` 是 `fetch(url)` 完成后的值
- `data` 是 `response.json()` 完成后的值

这也是 `async/await` 最大的可读性优势：
- 看起来像普通变量赋值
- 但本质仍然是异步流程

---

### 6. 为什么课程建议优先使用 `async/await`

对应视频时间：`01:51:30`

因为在大多数业务代码里，`async/await` 更适合人脑阅读：
- 顺序更清晰
- 嵌套更少
- 错误处理更集中

不过要补充一点：

`async/await` 并不是取代 Promise，  
它只是建立在 Promise 之上的更高层语法。

所以 Promise 基础仍然必须会。

---

## 十五、错误处理

### 1. 为什么错误处理是网络代码的必修内容

对应视频时间：`01:52:14`

网络请求不仅可能成功，也可能失败。失败原因很多：
- 没网
- 地址错了
- 服务器挂了
- 返回了错误状态码
- 返回的数据格式不符合预期

所以只写“成功逻辑”是不够的。

---

### 2. XHR 的错误处理

对应视频时间：`01:53:00`

XHR 常见做法是监听错误事件：

```js
xhr.addEventListener('error', () => {
  console.log('Network error');
});
```

同时也可以在 `load` 中检查状态码是不是成功。

这说明：
- 请求完成，不等于业务成功
- `load` 代表“响应到了”
- 但响应可能是错误响应

---

### 3. Promise 的 `.catch()`

对应视频时间：`01:56:00`

```js
fetch(url)
  .then((response) => {
    return response.json();
  })
  .catch((error) => {
    console.log('Unexpected error. Please try again later.');
  });
```

`.catch()` 的作用是集中处理 Promise 链中的失败情况。

补充理解：

`.catch()` 更像是“这条 Promise 链最后的错误出口”。

---

### 4. `async/await` 的 `try/catch`

对应视频时间：`01:58:20`

```js
async function loadPage() {
  try {
    const response = await fetch(url);
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.log('Unexpected error. Please try again later.');
  }
}
```

这是异步代码里非常常见的写法。

好处是：
- 成功逻辑放在 `try`
- 失败逻辑集中在 `catch`
- 结构很清晰

---

### 5. 需要区分两类失败

补充知识点。

初学者很容易把所有错误混成一类，但更准确的思路是区分：

1. 网络层失败
   - 请求没发成
   - 断网
   - 服务器不可达

2. 应用层失败
   - 请求发成了
   - 但返回 4xx / 5xx
   - 或返回的数据不符合业务要求

这两种失败在真实项目里通常会有不同提示和处理方式。

---

## 十六、把异步请求用到项目里

### 1. 并行加载商品和购物车

对应视频时间：`01:19:10`、`01:35:45`、`01:39:53`

项目里有两个典型数据源：
- 商品列表
- 购物车数据

它们可以并行请求，所以课程引入了 `Promise.all()`，后面又可以进一步改写成 `async/await`。

一个典型思路是：

```js
await Promise.all([
  loadProductsFetch(),
  loadCartFetch()
]);
```

等两边都准备好，再渲染页面。

---

### 2. 为什么数据加载完成后再渲染页面

补充知识点。

因为页面渲染依赖数据。

如果商品数据还没回来，你就：
- 计算价格
- 读取商品名称
- 渲染图片

就会出现：
- `undefined`
- 空白页面
- 报错

所以渲染通常应该放在“数据准备好之后”。

---

## 十七、创建订单与页面跳转

### 1. 创建订单是一次写操作

对应视频时间：`02:21:00`

这一段是项目里很关键的真实业务流程。

你不再只是读取数据，而是要把当前购物车信息提交给后端，让后端创建一笔订单。

这类操作和读取商品不同，因为它会改变服务器中的数据状态。

---

### 2. 把订单保存到本地

对应视频时间：`02:21:00` 到 `02:24:00`

课程里还把订单结果保存进本地 `orders` 数组，再同步到 `localStorage`。

这说明一个很常见的前端模式：
- 后端是权威数据来源
- 前端也可以在本地保存一份副本，方便页面快速读取

但要注意：

本地副本不是“真正的服务器数据库”，它只是当前浏览器里的缓存或备份。

---

### 3. 用 `window.location.href` 跳转页面

对应视频时间：`02:27:00`

```js
window.location.href = 'orders.html';
```

这表示：
- 修改当前页面地址
- 浏览器跳转到新页面

这是最基础的页面跳转方式之一。

---

## 十八、URL 参数 Query Params

### 1. 什么是 URL 参数

对应视频时间：`02:30:45`

URL 参数通常写在问号后面，例如：

```txt
tracking.html?orderId=123&productId=456
```

这里：
- `orderId=123`
- `productId=456`

它们是两组键值对。

用途是：
- 在页面跳转时顺便携带少量信息
- 让新页面知道自己该显示什么内容

---

### 2. 多个参数用 `&` 连接

对应视频时间：`02:36:00`

规则是：

```txt
?key1=value1&key2=value2&key3=value3
```

这在详情页、搜索页、分页页、tracking 页里都很常见。

---

### 3. 用内置 `URL` 类读取当前地址

对应视频时间：`02:33:00`

```js
const url = new URL(window.location.href);
```

这行代码会把当前页面完整地址解析成一个 URL 对象，方便读取其中各部分。

---

### 4. 用 `searchParams.get()` 获取参数

对应视频时间：`02:34:00`

```js
const orderId = url.searchParams.get('orderId');
const productId = url.searchParams.get('productId');
```

这是一种非常标准且推荐的读取方式。

好处是：
- 代码清晰
- 不需要手动切字符串
- 对多个参数也更容易维护

---

### 5. 为什么 tracking 页面需要 URL 参数

对应视频时间：`02:38:40`

因为 tracking 页面不是凭空显示内容，它需要知道：
- 要显示哪一笔订单
- 要跟踪订单里的哪个商品

这些信息最方便的传递方式之一，就是通过 URL 参数。

这也是“页面状态放进 URL”这一类前端设计思想的入门例子。

---

## 十九、回调、Promise、`async/await` 三者关系

### 1. 它们不是互相无关的三套东西

补充知识点。

可以把它们理解成三个层次：

1. 回调：最基础的异步表达方式
2. Promise：让异步结果可以被链式管理
3. `async/await`：让 Promise 写起来更像同步代码

所以学习顺序最好是：
- 先理解为什么异步要等待
- 再理解 Promise 的“未来结果”模型
- 最后用 `async/await` 提升可读性

---

### 2. 为什么不能只背语法

补充知识点。

如果你只背：
- `then`
- `await`
- `try/catch`

但没有建立“结果将来才回来”的心智模型，那么一换场景还是容易乱。

真正该掌握的是这句话：

> 异步代码的关键，不是语法，而是执行时机。

---

## 二十、本课容易混淆的点

### 1. `fetch()` 返回的不是最终数据

它返回的是 Promise，不是商品数组本身。

---

### 2. `response` 也不是最终 JSON 数据

`response` 是响应对象，通常还要再调用：

```js
await response.json();
```

---

### 3. `load` 不等于“一切都成功”

XHR 的 `load` 说明响应到了，但状态码可能仍然是错误。

---

### 4. `catch` 不代表业务逻辑就一定完整了

有些错误会进入 `catch`，但有些业务失败可能需要你自己根据状态码或响应内容判断。

---

### 5. `await` 不会让整个网页卡死

它只是暂停当前 `async` 函数，不是暂停整个 JavaScript 世界。

---

### 6. URL 参数本质上是字符串

如果你要拿它做数字计算，通常还要自己转换类型。

---

## 二十一、这节课应该额外补充理解的知识

### 1. API 文档不是可选项

当你和后端协作时，文档能告诉你：
- 路径
- 方法
- 参数
- 返回格式
- 错误格式

不会看文档，网络请求通常就写不稳。

---

### 2. “读取数据”和“修改数据”最好分开理解

这节课里你已经碰到了两类典型操作：
- 读取商品数据
- 创建订单

前者通常是读操作，后者通常是写操作。  
它们在真实项目里常常对应不同的 HTTP 方法和错误处理策略。

---

### 3. 页面跳转和数据流要一起考虑

不是“跳转了就结束”，而是要考虑：
- 新页面需要哪些数据
- 这些数据从哪里来
- 是通过 URL 传，还是重新请求后端

tracking 页面就是一个典型例子。

---

## 二十二、本课最重要的结论

1. 后端是负责数据和业务处理的另一台计算机
2. 前端和后端通过 HTTP 请求和响应通信
3. XHR 能帮助你理解最基础的请求流程
4. `fetch` 是现代浏览器里更常用的请求方式
5. Promise 表示未来会完成的结果
6. `async/await` 让 Promise 代码更清晰
7. 错误处理必须成为网络代码的一部分
8. URL 参数是页面传递少量信息的常用方案
9. 异步编程最核心的是“等结果回来再继续”

---

## 二十三、建议复习顺序

1. 先重新理解前端、后端、HTTP 请求和响应
2. 再复习 `XMLHttpRequest` 的完整流程
3. 然后理解为什么网络代码天然是异步的
4. 再依次复习回调、Promise、`fetch`、`async/await`
5. 最后回到 Amazon 项目，重新看“加载数据、创建订单、跳转 tracking 页面”整条业务线

---

## 二十四、课后练习建议

1. 用 `XMLHttpRequest` 请求一个文本接口，并在 `load` 事件里打印结果
2. 用 `fetch()` 重写同样的请求
3. 写一个返回 Promise 的函数，并用 `.then()` 获取结果
4. 用 `async/await` 改写上一步函数
5. 给异步请求补上 `try/catch`
6. 构造一个带 `orderId` 和 `productId` 的 URL，并在页面中读出参数
7. 自己总结“回调、Promise、async/await”的关系，用一句话分别解释三者

---

## 二十五、给初学者的最终提醒

这一课最容易让人觉得“突然变难”，不是因为语法很多，而是因为你开始接触真实 Web 开发里的时间问题。

从这节课开始，你需要逐渐习惯：

- 数据不一定立刻可用
- 页面往往依赖远程数据
- 请求可能成功也可能失败
- 页面跳转后仍然要考虑数据如何延续

如果你把这些思路真正搞明白，后面的课程无论继续讲 Node.js、后端、框架还是更复杂的项目，都会顺很多。
