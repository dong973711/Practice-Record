package com.how2java.util;

public class Page {
	int start = 0;
	int count = 5;
	int last = 0;

	public int getStart() {
		return start;
	}

	public void setStart(int start) {
		this.start = start;
	}

	public void setCount(int count) {
		this.count = count;
	}

	public int getLast() {
		return last;
	}

	public void setLast(int last) {
		this.last = last;
	}

	public int getup() {
		int next = this.start-this.count;
		if(next<0){
			System.out.println("已经到顶了，不能再上一页了");
			return this.start;
		}
		else {
			return next;
		}
	}
	public int getdown() {
		int next = this.start+this.count;
		if(next>this.last){
			System.out.println("已经到低了，不能再下一页了");
			return this.start;
		}
		else {
			return next;
		}
	}
	public void caculateLast(int total) {
		if (0 == total % count)
			last = total - count;
		else
			last = total - total % count;
	}
}
