package com.how2java.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import com.github.pagehelper.PageHelper;
import com.github.pagehelper.PageInfo;
import com.how2java.entity.Category;
import com.how2java.service.CategoryService;
import com.how2java.util.Page;

@Controller
@RequestMapping("")
public class CategoryController {
	@Autowired
	CategoryService categoryservice;

	@RequestMapping("listCategory")
	public ModelAndView listCategory(Page page) {
		ModelAndView mav = new ModelAndView();
		PageHelper.offsetPage(page.getStart(), 5);
		List<Category> cs = categoryservice.list();
		int total = (int)new PageInfo<>(cs).getTotal();
		page.caculateLast(total);
		mav.addObject("category", cs);//放入转发参数
		mav.setViewName("listCategory");//放入jsp路径
		return mav;
	}
	
	@RequestMapping("addCategory")
	public ModelAndView addCategory(Category category) {
		
		int res = categoryservice.add(category);
		if(res>0)
			System.out.println("添加成功");
		ModelAndView mav = new ModelAndView("redirect:/listCategory");
		return mav;
		
	}
	@RequestMapping("editCategory")
	public ModelAndView editCategory(Category category) {
		Category c = categoryservice.get(category.getId());
		ModelAndView mav = new ModelAndView("editCategory");
		mav.addObject("c",c);
		return mav;
	}
	@RequestMapping("updateCategory")
	public ModelAndView updateCategoey(Category category) {
		
		int res = categoryservice.update(category);
		if(res>0)
			System.out.println("更新成功");
		ModelAndView mav = new ModelAndView("redirect:/listCategory");
		return mav;
		
	}
	@RequestMapping("deleteCategory")
	public ModelAndView deleteCategory(Category category) {
		
		categoryservice.delete(category);
		ModelAndView mav = new ModelAndView("redirect:/listCategory");
		return mav;
		
	}
}
