package com.how2java.mapper;

import java.util.List;

import com.how2java.entity.Category;

public interface CategoryMapper {
	public int add(Category category);

	public void delete(Category category);

	public Category get(int id);

	public int update(Category category);

	public List<Category> list();

	public int count();
	
//	public List<Category> list(Page page);
//
//	public int total();
}
