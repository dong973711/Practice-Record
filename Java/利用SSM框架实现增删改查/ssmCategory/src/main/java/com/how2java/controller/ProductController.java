package com.how2java.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import com.github.pagehelper.PageHelper;
import com.github.pagehelper.PageInfo;
import com.how2java.entity.Product;
import com.how2java.service.ProductService;
import com.how2java.util.Page;

@Controller
@RequestMapping("")
public class ProductController {
	@Autowired
	ProductService productsevice;
	
	@RequestMapping("listProduct")
	public ModelAndView listProduct(Page page) {
		ModelAndView mav = new ModelAndView();
		PageHelper.offsetPage(page.getStart(), 5);
		List<Product> list = productsevice.list();
		int total = (int)new PageInfo<>(list).getTotal();
		page.caculateLast(total);
		mav.addObject("products",list);
		mav.setViewName("listProduct");
		return mav;
	}
	@RequestMapping("addProduct")
	public ModelAndView addProduct(Product p) {
		productsevice.add(p);
		ModelAndView mav = new ModelAndView("redirect:/listProduct");
		return mav;
	}
	@RequestMapping("deleteProduct")
	public ModelAndView deleteProduct(int id) {
		Product p = productsevice.get(id);
		productsevice.delete(p);
		ModelAndView mav = new ModelAndView("redirect:/listProduct");
		return mav;
	}
	@RequestMapping("editProduct")
	public ModelAndView editProduct(int id) {
		Product p = productsevice.get(id);
		System.out.println("将要修改的product是："+p.toString());
		ModelAndView mav = new ModelAndView("editProduct");
		mav.addObject("product",p);
		return mav;
	}
	@RequestMapping("updateProduct")
	public ModelAndView updateProduct(Product product) {
		System.out.println("到这里了"+product.toString());
		int rst = productsevice.update(product);
		if(rst>0)
			System.out.println("更新成功");
		else
			System.out.println("更新失败");
		ModelAndView mav = new ModelAndView("redirect:/listProduct");
		return mav;
	}
//	@RequestMapping("updateProduct")
//	public ModelAndView updateProduct(Product product){
//		productsevice.update(product);
//		ModelAndView mav = new ModelAndView("redirect:/listProduct?id="+product.getCategory().getId());
//		return mav;
//	}	
}
