package com.how2java.service.impl;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.how2java.entity.Category;
import com.how2java.mapper.CategoryMapper;
import com.how2java.service.CategoryService;

@Service
public class CategoryServiceImpl implements CategoryService {

	@Autowired
	CategoryMapper categorymapper;
	
	@Override
	public List<Category> list() {
		return categorymapper.list();
	}

	@Override
	public int add(Category category) {
		return categorymapper.add(category);
	}

	@Override
	public int update(Category category) {
		return categorymapper.update(category);
	}

	@Override
	public void delete(Category category) {
		categorymapper.delete(category);
	}
	public Category get(int id) {
		return categorymapper.get(id);
	}
	

//	@Override
//	public int total() {
//		return categorymapper.total();
//	}
//
//	@Override
//	public List<Category> list(Page page) {
//		return categorymapper.list(page);
//	}

}
