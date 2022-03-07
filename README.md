### 体育场馆自动预约

声明：本脚本仅供学习技术使用，作者不承担一切因使用此脚本或相关衍生物带来的影响

### 使用方法

- 根据自己chrome的版本和操作系统下载对应的[chromedrive](http://chromedriver.storage.googleapis.com/index.html)
- python拓展依赖
  - selenium
  - numpy
  - easyocr【可能第一次运行程序需要连接vpn下载相关reader文件】
  - pillow

在脚本对应位置填写相关信息，利用本机操作系统设定定时任务即可安心睡觉。作者测试执行一次抢场任务大概10s左右【绝大多数时间在ocr识别上】。目前脚本内只有正大羽毛球的两个url，如果需要使用其他服务，修改url内contentId即可。

### 远程验证码识别

如果您无法安装easyocr——它依赖于麻烦的pytorch，可以尝试使用[图鉴](http://www.ttshitu.com/)的识图服务，注册账号并充值一定金额，在脚本remote_xx处填上用户名和密码即可。