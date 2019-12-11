
# 流程：
**实体类(Category.java)**->
**mapper(CategoryMapper.java)**(接口类，定义各个功能)->
**xml(Category.xml)**(利用sql语句实现mapper接口类中的方法)->
**service(CategoryService.java)**(接口类)->
**serviceimpl(CategoryServiceImpl.java)**(继承service接口类，并利用mapper的中的方法实现，因为mapper中的方法再xml中也实现了)(被注解@Service标示为一个Service并且装配了Mapper)->
**controller(CategoryController)**(Controller被@Controller标示为了控制器，自动装配了Service，通过@RequestMapping映射访问路径/xxx路径到方法yyy ()。在yyy()方法中，通过Service获取后，然后存放在"cs"这个key上。)
![](/项目结构图1.png)
![](/项目结构图2.png)
![](/listCategory.png)
![](/listProduct.png)
# 思路：
1. 首先浏览器上访问路径 /listCategory
2. tomcat根据web.xml上的配置信息，拦截到了/listCategory，并将其交由DispatcherServlet处理。
3. DispatcherServlet 根据springMVC的配置，将这次请求交由CategoryController类进行处理，所以需要进行这个类的实例化
4. 在实例化CategoryController的时候，注入CategoryServiceImpl。 (自动装配实现了CategoryService接口的的实例，只有CategoryServiceImpl实现了CategoryService接口，所以就会注入CategoryServiceImpl)
5. 在实例化CategoryServiceImpl的时候，又注入CategoryMapper
6. 根据ApplicationContext.xml中的配置信息，将CategoryMapper和Category.xml关联起来了。
7. 这样拿到了实例化好了的CategoryController,并调用 list 方法
8. 在list方法中，访问CategoryService,并获取数据，并把数据放在"cs"上，接着服务端跳转到listCategory.jsp去
9. 最后在listCategory.jsp 通过后端传来的“cs”显示数据


# 思路图：
![思路图](https://stepimagewm.how2j.cn/4518.png)


[学习网站](https://how2j.cn/)