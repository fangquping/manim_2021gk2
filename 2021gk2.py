from manimlib.imports import *

class Question(Scene):#该类用于显前提公式
    CONFIG={"camera_config":{"background_color":WHITE}}
    def construct(self):
        q4=TextMobject(
            "4. 卫星导航系统中，地球静止同步轨道卫星的轨道位于地球赤道所在平面，\\\\",
            "轨道高度为36000km（轨道高度指卫星到地球表面的最短距离），把地球看\\\\",
            "作是球心为$O$半径$r$为6400km的球，其上点$A$的纬度是指$OA$与赤道\\\\",
            "所在平面所成角的度数，地球表面能直接观测到的一颗地球静止同步轨道\\\\",
            "卫星的点的纬度的最大值记为$\\alpha$，该卫星信号覆盖的地球表面面积\\\\",
            "$S=2\\pi r^2(1-\\cos\\alpha)$.（单位：km²），则S占地球表面积的百分比为\\\\",
            "A$\ 26\\%\ \ $B$\ 34\\%\ \ $C$\ 42\\%\ \ $D$\ 50\\% $",
            background_stroke_color=WHITE
        )

        q4.set_color(BLACK)
        q4.arrange_submobjects(
            DOWN,
            aligned_edge=LEFT
        )
        q4.scale(0.74)
        q4.to_edge(UL)
        q4[6].shift(DOWN)
    
        self.play(FadeIn(q4))
        self.wait(8)

        self.play(FadeOutAndShift(q4,RIGHT))#将题弄出去
        
        qp=TexMobject(
            "{S\\over 4\\pi r^2}&={2\\pi r^2(1-\\cos \\alpha)\\over 4\\pi r^2}\\\\",
            "&={1-\\cos\\alpha\\over 2}\\\\",
            "\\cos\\alpha &=\\frac{6400}{36000+6400}\\\\",
            "&=\\frac{8}{45+8}\\approx 0.1509\\\\",#3
            "\\therefore &{1-\\cos\\alpha\\over 2}\\approx 42\\%\\\\",
            background_stroke_color=WHITE
        )

        qp.set_color(BLACK)
        """
        qp.arrange_submobjects(
            DOWN,
            aligned_edge=LEFT
        )
        """
        qp.to_edge(UL)

        [self.play(Write(qp[k])) for k in range(5)] #显示过程

        self.wait(4)

        q4l=TextMobject("选择C",background_stroke_color=RED)
        q4l.set_color(RED_B)
        q4l.shift(DOWN+RIGHT)
        self.play(FadeOut(qp))
        self.play(FadeIn(q4))

        self.play(FadeIn(q4l))
        self.wait()
        self.play(FadeOut(q4))#退出题
        self.play(FadeOut(q4l))#退出答案



class ThreeD(ThreeDScene):
    CONFIG={"camera_config":{"background_color":WHITE}}
    def construct(self):
        
        c1=ParametricSurface(
            lambda u,v :np.array([
                2*np.cos(u),2*np.cos(v)*np.sin(u),2*np.sin(v)*np.sin(u)
            ]),
            v_min=0,v_max=TAU,u_max=PI,u_min=66.4*DEGREES,
            checkerboard_colors=[PURPLE_D,PURPLE_D],
            resolution=(20,20)
        )
        """
        cp=ParametricSurface(
            lambda u,v:np.array([.8,u,v]),
            v_min=-3,v_max=3,u_min=-3,u_max=3,
            checkerboard_colors=[RED_D,RED_D],
            resolution=(16,16)
        )#平面
        """
        cz=ParametricSurface(
            lambda u,v:np.array([
                u,
                u*np.tan(66.4*DEGREES)*np.cos(v),
                u*np.tan(66.4*DEGREES)*np.sin(v)
            ]),
            u_min=0,u_max=.8,v_min=0,v_max=TAU,
            checkerboard_colors=[RED_D,RED_D],
            resolution=(20,20)
        )#圆锥
        cz1=ParametricSurface(
            lambda u,v:np.array([
                2*np.cos(u),
                2*np.sin(u)*np.cos(v),
                2*np.sin(u)*np.sin(v)
            ]),
            u_min=0,u_max=66.4*DEGREES,v_min=0,v_max=TAU,
            checkerboard_colors=[RED_D,RED_D],
            resolution=(20,20)
        )#球缺面
        #cz1.shift(RIGHT)#挪动一下
        

        self.set_camera_orientation(phi=120*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)
        
        self.play(FadeIn(cz1),FadeIn(cz))
        self.wait(2)
        self.play(FadeIn(c1))
        self.wait(4)#FadeIn(cp),FadeIn(cz)
        
        self.play(FadeOut(c1),FadeOut(cz1),FadeOut(cz))#退出

        cz.set_color(BLUE_D)#圆锥

        self.play(FadeIn(cz1),FadeIn(cz))#再显示内容

        self.wait(14)



class Qs(Scene):#该类用于显前提公式
    CONFIG={"camera_config":{"background_color":WHITE}}
    def construct(self):
        t=TextMobject(
            "上面球体部分体积为：\\\\",#0
            " $$\\pi r^2(r-r\\cos \\alpha) -\\left [\\frac{1}{3}\\pi r^3-\\frac{1}{3}\\pi(r\\cos\\alpha)^3\\right ] $$ \\\\",
            " $$=$$",#2
            " $$\\pi r^2(r-r\\cos \\alpha) -\\frac{1}{3}\\pi r^3+\\frac{1}{3}\\pi r^3\\cos ^3\\alpha $$ \\\\",
            "下部分圆锥体积为：\\\\",
            " $$\\frac{1}{3}\\pi r^2\\sin ^2\\alpha\\cdot r\\cos \\alpha $$ ",
            " $$=$$",#6
            " $$\\frac{1}{3}\\pi r^3\\cos \\alpha \\sin ^2\\alpha $$\\\\",
            " 球底圆锥体积为：\\\\",#8
            " $$+$$ ",#9
            " $$=\\pi r^3\\left (\\frac{2}{3}-\\cos \\alpha +\\frac{1}{3}\\cos ^3\\alpha +\\frac{1}{3}\\cos\\alpha\\sin^2\\alpha\\right )$$ ",
            " $$=\\frac{2}{3}\\pi r^3(1-\\cos\\alpha)$$ ",#11
            " $$\\therefore S={\\frac{2}{3}\\pi r^3(1-\\cos\\alpha) \\over \\frac{4}{3}\\pi r^3}\\cdot 4\\pi r^2=2\\pi r^2(1-\\cos\\alpha)$$ ",
            background_stroke_color=WHITE
        )

        t.set_color(BLACK)
        t.arrange_submobjects(
            DOWN,
            aligned_edge=LEFT
        )
        t.to_edge(UL)#设置位置
        t[2].shift(DOWN*.3)
        t[3].next_to(t[2])
        
        t[4:].shift(.7*UP)

        t[6].shift(DOWN*.3)
        t[7].next_to(t[6])
        t[8:].shift(.7*UP)

        [self.play(Write(ko),run_time=1.6) for ko in t[:8] ]
        self.wait(4)

        self.play(FadeOutAndShift(t[0:3],LEFT),FadeOutAndShift(t[4:7],LEFT))#退出文字部分
        self.play(t[3].to_edge,UL)
        self.play(t[7].shift,4*UP+.7*LEFT)

        self.wait()

        t[8:].shift(4*UP)
        self.play(FadeInFrom(t[8],LEFT))#写出下部分
        self.play(t[3].shift,3*DOWN)
        self.play(t[9].next_to,t[3])
        self.play(t[7].next_to,t[9])
        self.wait()#写出终极式子

        self.play(t[8].shift,2.3*UP)
        ft=VGroup(t[3],t[7],t[9])
        self.play(ft.shift,2.3*UP)
        self.wait()

        t[10:].shift(1.8*UP)
        [self.play(Write(ko)) for ko in t[10:12]]
        self.wait()

        self.play(FadeInFrom(t[12],UP))

        self.wait(4)



class Tsp(ThreeDScene):
    CONFIG={"camera_config":{"background_color":WHITE}}
    def construct(self):
        
        cz=ParametricSurface(
            lambda u,v:np.array([
                u,
                u*np.tan(66.4*DEGREES)*np.cos(v),
                u*np.tan(66.4*DEGREES)*np.sin(v)
            ]),
            u_min=0,u_max=.8,v_min=0,v_max=TAU,
            checkerboard_colors=[PURPLE_D,PURPLE_D],
            resolution=(16,16)
        )#圆锥
        cz1=ParametricSurface(
            lambda u,v:np.array([
                2*np.cos(u),
                2*np.sin(u)*np.cos(v),
                2*np.sin(u)*np.sin(v)
            ]),
            u_min=0,u_max=66.4*DEGREES,v_min=0,v_max=TAU,
            checkerboard_colors=[PURPLE_D,PURPLE_D],
            resolution=(16,16)
        )#球缺面

        cp=ParametricSurface(
            lambda u,v:np.array([
                .8,u*np.cos(v),u*np.sin(v)
            ]),
            v_min=0,v_max=TAU,u_min=0,u_max=1.833,
            checkerboard_colors=[PURPLE_D,PURPLE_D],
            resolution=(16,16)
        )#圆面
        cp1=cp.copy()

        self.set_camera_orientation(phi=75*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)#设置3d造型

        self.play(FadeIn(cz),FadeIn(cz1))

        ballq=VGroup(cz,cp)#圆锥体
        ballv=VGroup(cz1,cp1)#球缺与下面
        self.wait(3)

        self.play(ballv.shift,.5*RIGHT)
        self.play(ballq.shift,.5*LEFT)

        self.wait(9)
        self.play(FadeOut(ballq))#退出圆锥体

        cpzp=ParametricSurface(
            lambda u,v:np.array([
                2,u*np.cos(v),u*np.sin(v)
            ]),
            v_min=0,v_max=TAU,u_min=0,u_max=2,
            checkerboard_colors=[BLUE_D,BLUE_D],
            resolution=(16,16)
        )#圆柱底面
        cp.shift(1.7*RIGHT)#将圆锥底面作为圆柱底面的渐变面
        cp.set_color(BLUE_D)

        czhu=ParametricSurface(
            lambda u,v:np.array([
                u,
                2*np.cos(v),
                2*np.sin(v)
            ]),
            u_min=.8,u_max=2,v_min=0,v_max=TAU,
            checkerboard_colors=[BLUE_D,BLUE_D],
            resolution=(16,16)
        )#圆柱
        self.play(ballv.shift,.5*LEFT)
        self.play(ShowCreation(czhu))#显示圆柱
        self.play(ShowCreation(cpzp))#显示圆柱底面（原圆锥底面）
        self.wait()#等待1秒，作底面渐变
        self.play(ReplacementTransform(cpzp,cp))
        self.play(FadeOut(cp))#慢慢关掉底面

        self.wait(2)



class MoveObj(Scene):#该类用于显前提公式
    CONFIG={"camera_config":{"background_color":WHITE}}
    def construct(self):
        tx=TextMobject(
            "截面环形面积","截面圆形面积","正面图","侧面图",
            background_stroke_color=BLACK
        )
        tx.set_color(BLACK)

        tc=TexMobject(
            "\\pi (r^2-h^2)","\\pi r^2-\\pi h^2",
            background_stroke_color=WHITE
            )
        tc.set_color(BLACK)

        l0=Line(
            np.array([.4,2.75,0]),np.array([.4,2.1665,0]),
            #stroke_width=.8
        )
        l1=Line(
            np.array([.4,.3335,0]),np.array([.4,-.25,0]),
            #stroke_width=.8
        )
        l2=Line(
            np.array([.4,-2.25,0]),np.array([.4,-2.75,0]),
            #stroke_width=.8
        )
        VGroup(l0,l1,l2).set_color(GREY)#灰色直线

        la=Line(
            np.array([.4,-.25,0]),np.array([.4,-.85,0]),
            #stroke_width=.8
        )
        lb=Line(
            np.array([.4,-1.65,0]),np.array([.4,-2.25,0]),
            #stroke_width=.8
        )#l1,2,3是外面的竖，la，b是形内竖
        la.set_color(PURPLE_D)
        lb.set_color(PURPLE_D)

        lr=Line(
            np.array([.4,2.1665,0]),np.array([.4,.3335,0]),
            #stroke_width=.8
        )
        lr.set_color(PURPLE_D)
        #圆截面
        lrr=Line(
            np.array([.4,-.85,0]),np.array([.4,-1.65,0]),
            #stroke_width=.8
        )
        lrr.set_color(GREY)
        #圆锥体空
        lo=DashedLine(np.array([0,0,0]),np.array([.4,0,0]) )
        lo.set_color(RED_D)

        circle=Sector(
            arc_center=np.array([0,1.25,0]),
            radius=1.,
            start_angle=-.5*PI,
            angle=PI,fill_color=GREEN,fill_opacity=.8,
            stroke_color=BLUE,stroke_width=4
        )

        triangle=Polygon(
            np.array([0,-.25,0]),np.array([0,-2.25,0]),
            np.array([1,-2.25,0]),np.array([0,-1.25,0]),np.array([1,-.25,0])
        )
        triangle.set_fill(color=GREEN,opacity=.6)

        rect=Rectangle(
            height=2,width=1,
            #fill_color=GREEN,opacity=.6,
            stroke_width=4,stroke_color=BLUE
        )
        rect.set_fill(color=GREEN,opacity=.6)
        rect.shift(.5*RIGHT+1.25*DOWN)#背景形状

        cc0=Circle(
            arc_center=np.array([3,1.25,0]),
            radius=.916515,
            stroke_color=PURPLE_D,fill_color=GREEN,fill_opacity=.8
        )
        ccb=Circle(
            arc_center=np.array([3,-1.25,0]),
            radius=1.,
            stroke_color=PURPLE_D,fill_color=GREEN,fill_opacity=.8
        )#圆背景
        cc1=Circle(
            arc_center=np.array([3,-1.25,0]),
            radius=.4,
            stroke_color=PURPLE_D,fill_color=WHITE,fill_opacity=1.
        )#添加圆

        self.play(FadeIn(circle),FadeIn(cc0))
        self.play(
            FadeIn(rect),FadeIn(triangle),
            FadeIn(ccb),FadeIn(cc1),
        )#添加环形

        everyt=4/11#时间单位1
        self.play(ShowCreation(l0,run_time=everyt* .5835),rate_func=linear)
        self.play(ShowCreation(lr,run_time=everyt* .833),rate_func=linear)
        self.play(ShowCreation(l1,run_time=everyt*.5835),rate_func=linear)
        self.play(ShowCreation(la,run_time=everyt*.6),rate_func=linear)
        self.play(ShowCreation(lrr,run_time=everyt* .8),rate_func=linear)
        self.play(ShowCreation(lb,run_time=everyt* .6),rate_func=linear)
        self.play(ShowCreation(l2,run_time=everyt*.5),rate_func=linear)
        self.play(FadeIn(lo,run_time=.6))
        #按顺序画竖线

        #lineSum=VGroup(l0,lr,l1,la,lrr,lb,l2)

        def moreX(onj):
            x=lo.get_center()*2
            x=np.inner(x,np.array([1,0,0]))
            t=np.sqrt(1-x**2)
            onj.put_start_and_end_on(np.array([x,2.75,0]),np.array([x,1.25+t,0]))
            """
            onj[1].put_start_and_end_on(np.array([x,1.25+t,0]),np.array([x,1.25-t,0]))
            onj[2].put_start_and_end_on(np.array([x,1.25-t,0]),np.array([x,-.25,0]))

            onj[3].put_start_and_end_on(np.array([x,-.25,0]),np.array([x,-1.25+x,0]))
            onj[4].put_start_and_end_on(np.array([x,-1.25+x,0]),np.array([x,-1.25-x,0]))
            onj[5].put_start_and_end_on(np.array([x,-1.25-x,0]),np.array([x,-2.25,0]))

            onj[6].put_start_and_end_on(np.array([x,-2.25,0]),np.array([x,-2.75,0]))
            """
        
        l0.add_updater(moreX)#挪动情况
        
        def moreXr(onk):
            x=lo.get_center()*2
            x=np.inner(x,np.array([1,0,0]))
            if x>.9999:
                self.remove(onk)
            else:
                t=np.sqrt(1-x**2)
                onk.put_start_and_end_on(np.array([x,1.25+t,0]),np.array([x,1.25-t,0]))
        
        lr.add_updater(moreXr)#挪动情况

        
        def moreX1(onj):
            x=lo.get_center()*2
            x=np.inner(x,np.array([1,0,0]))
            t=np.sqrt(1-x**2)
            onj.put_start_and_end_on(np.array([x,1.25-t,0]),np.array([x,-.25,0]))

        
        def moreXa(onj):
            x=lo.get_center()*2
            x=np.inner(x,np.array([1,0,0]))
            if x>.9999:
                self.remove(onj)
            else:
                onj.put_start_and_end_on(np.array([x,-.25,0]),np.array([x,-1.25+x,0]))
           
        
        def moreXrr(onj):
            x=lo.get_center()*2
            x=np.inner(x,np.array([1,0,0]))
            onj.put_start_and_end_on(np.array([x,-1.25+x,0]),np.array([x,-1.25-x,0]))
        
        def moreXb(onj):
            x=lo.get_center()*2
            x=np.inner(x,np.array([1,0,0]))
            if x>.9999:
                self.remove(onj)
            else:
                onj.put_start_and_end_on(np.array([x,-1.25-x,0]),np.array([x,-2.25,0]))
        
        def moreX2(onj):
            x=lo.get_center()*2
            x=np.inner(x,np.array([1,0,0]))

            onj.put_start_and_end_on(np.array([x,-2.25,0]),np.array([x,-2.75,0]))
        
        
        l1.add_updater(moreX1)
        la.add_updater(moreXa)
        lrr.add_updater(moreXrr)
        lb.add_updater(moreXb)
        l2.add_updater(moreX2)#全部加上update

        def moreS(obj):
            x=lo.get_center()*2
            x=np.inner(x,np.array([1,0,0]))
            if x>.9999:
                self.remove(obj)
            else:
                t=np.sqrt(1-x**2)
                obj.scale(t/.916515)
        
        cc0.add_updater(moreS)
        
        def moreS1(obj):
            x=lo.get_center()*2
            x=np.inner(x,np.array([1,0,0]))
            if x>.9999:
                obj.become(
                    Circle(
                        arc_center=np.array([3,-1.25,0]),
                        stroke_color=WHITE,fill_color=WHITE,fill_opacity=1.,
                        radius=1
                    )   
                )
                self.remove(ccb)
            else:
                obj.become(Circle(
                    arc_center=np.array([3,-1.25,0]),
                    stroke_color=PURPLE_D,fill_color=WHITE,fill_opacity=1.,
                    radius=x 
                ))
        
        cc1.add_updater(moreS1)

        self.play(lo.put_start_and_end_on,np.array([0,0,0]),np.array([1,0,0]))#挪动h
        #self.play(lo.put_start_and_end_on,np.array([0,0,0]),np.array([.1,0,0]))
        self.wait(2)


        
