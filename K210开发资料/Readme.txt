1、如果文件夹内有readme文件，请务必先阅读readme

2、本文档只为方便客户使用，没有办法保证是最新的文件，熟悉整个流程后，请上以下两个网站看是否有对应的更新的文件
	https://github.com/kendryte
	https://kendryte.com/downloads/

3、目前有两种sdk，一种是standalone,一种是freertos，推荐用standalone
请下载develop分支：
https://github.com/kendryte/kendryte-standalone-sdk
https://github.com/kendryte/kendryte-standalone-demo
sdk说明参考如下：
https://github.com/kendryte/kendryte-doc-standalone-programming-guide/tree/master/zh-Hans

4、在线调试方法参考论坛上的链接https://forum.kendryte.com/topic/181/a-guide-to-setup-command-line-development-environment-for-k210/9

5、运行算法的一些例子：
kendryte-standalone-demo下有face_dect（人脸检测）和kpu（20分类）的例子

6、算法模型转换参考以下：
https://github.com/kendryte/nncase/blob/master/docs/USAGE_ZH.md

7、模型转换工具下有一些例子展示了如何部署算法到芯片：
https://github.com/kendryte/nncase/tree/master/examples
20classes_yolo	
facedetect_landmark
fast_facedetect
iris

8、开发板可以从官方淘宝店直接购买：
https://item.taobao.com/item.htm?spm=a230r.1.14.19.3eef2126DUolri&id=578293728873&ns=1&abbucket=14#detail

9、摄像头已经调通的sensor: ov5640/0v2640/gc0328/gc0308