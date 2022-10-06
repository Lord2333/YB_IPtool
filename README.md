# YB_IPtool
A simple network tool for Yiban.

main.py是有gui版本的主程序脚本，直接运行Functions.py就是命令行版本

## 使用

首先注册[芝麻代理](https://www.zmhttp.com)，进行实名认证。

然后打开软件，点击“链接IP池”，根据提示将当前设备IP地址添加到芝麻代理白名单中，然后去领取每日白嫖套餐；

![](https://s2.loli.net/2022/10/06/CDdExFAYgRaql2e.gif)

![](https://s2.loli.net/2022/10/06/BdputSkRTMI3Xej.png)

然后重新点击按钮，出现下面提示则说明已经添加成功；

![](https://s2.loli.net/2022/10/06/RTJo8r3F4whVkPi.png)

然后打开要刷访问量的轻应用页面，在地址栏中复制他的Appid，即`https://q.yiban.cn/my/myDevAppDetail/appid/1234567`链接中的`1234567`就是这个轻应用的Appid，填写到下面的文本框中点击提交，输入要刷的访问量，即可开始运行。

> 注：填写的访问量不能小于50，填写的值与实际刷到的值可能会存在10%左右的偏差，通常都会小于输入的值，这个偏差与请求速度有关系，似乎对同一个轻应用的请求超过某一个阈值就会被视作DDos攻击，暂时不清楚这个阈值是多少，有能力的同学可以自行修改源代码里的时间间隔进行尝试。

![](https://s2.loli.net/2022/10/06/1TUS5kJPAbcj2ax.png)

![](https://s2.loli.net/2022/10/06/246XGwutFjW3Umo.png)

注意：在程序运行时，请勿最小化程序窗口！！！

运行效果如图：运行前

![运行前](https://s2.loli.net/2022/10/06/7Oy3z2usjRoFVfW.png)

运行后

![](https://s2.loli.net/2022/10/06/7BEegrpw3ODySv6.png)

![](https://s2.loli.net/2022/10/06/X51OQf9bxWlRcEk.png)
