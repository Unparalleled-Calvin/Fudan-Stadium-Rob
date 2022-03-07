### 体育场馆自动预约

声明：本脚本仅供学习技术使用，作者不承担一切因使用此脚本或相关衍生物带来的影响

### 使用方法

- 下载[chromedrive.exe](http://chromedriver.storage.googleapis.com/index.html)
- python拓展依赖
  - selenium
  - numpy
  - easyocr【可能第一次使用需要连接vpn下载相关reader文件】
  - pillow

在脚本对应位置填写相关信息，利用本机操作系统设定定时任务即可安心睡觉。作者测试执行一次抢场任务大概10s左右【绝大多数时间在ocr识别上】。目前脚本内只有正大羽毛球的两个url，如果需要使用其他服务，修改url内contentId即可。