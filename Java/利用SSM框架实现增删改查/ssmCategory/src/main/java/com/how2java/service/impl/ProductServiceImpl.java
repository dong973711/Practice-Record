package com.how2java.service.impl;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.how2java.entity.Product;
import com.how2java.mapper.ProductMapper;
import com.how2java.service.ProductService;

@Service
public class ProductServiceImpl implements ProductService{

	@Autowired
	ProductMapper productmapper;
	@Override
	public int add(Product p) {
		return productmapper.add(p);
	}
	@Override
	public List<Product> list() {
		List<Product> p = productmapper.list();
		return p;
	}
	@Override
	public void delete(Product product) {
		productmapper.delete(product);
		
	}
	@Override
	public Product get(int id) {
		return productmapper.get(id);
	}
	@Override
	public int update(Product p) {
		return productmapper.update(p);
	}
	
	

}
