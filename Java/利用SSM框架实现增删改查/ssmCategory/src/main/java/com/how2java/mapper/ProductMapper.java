package com.how2java.mapper;

import java.util.List;

import com.how2java.entity.Product;

public interface ProductMapper {
	public int add(Product p);
	
	public void delete(Product p);
	
	public Product get(int id);
	
	public int update(Product p);
	
	public List<Product> list();
}
