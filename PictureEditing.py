from PIL import Image
import numpy as np
def GetPicture():#获取图片文件
    npic=input("请输入图片地址:")
    return npic
def GetDepth():
    try:
        depth=eval(input("图像修改的强度(范围0~100,推荐10)："))
        if depth>100:
            return 100
        elif depth<0:
            return 0
        else:
            return depth
    except:
        print("输入错误!")
def GetGrad(npic):#获取图像灰度的阶梯值
    try:
        im=Image.open(npic).convert('L')
        arr=np.asarray(im).astype('float')
        grad=np.gradient(arr)
        return grad
    except:
        print('地址错误!')
def main():
    el=np.pi/2.2#光源的俯视角度
    az=np.pi/4.0#光源的方位角度
    print("**制作图片手绘效果**")
    npic=GetPicture()
    depth=GetDepth()
    grad=GetGrad(npic)
    x,y=grad
    x=x*depth/100.0
    y=y*depth/100.0#修改横纵坐标图像梯度值
    dx=np.cos(el)*np.cos(az)
    dy=np.cos(el)*np.sin(az)
    dz=np.sin(el)
    a=np.sqrt(x**2+y**2+1.0)
    u_x=x/a
    u_y=y/a
    u_z=1.0/a
    a1=255*(dx*u_x+dy*u_y+dz*u_z)#光源归一化
    a1=a1.clip(0,255)
    IM=Image.fromarray(a1.astype('uint8'))#重构图像
    IM.save('NewPicture.jpg')
    print('制作成功！')
main()