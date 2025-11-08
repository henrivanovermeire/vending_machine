#include <stdio.h>

struct Item {
	char name[128];
	int price;
};

struct VendingMachine{
	void activate() {
		printf("Vending machine activated!\n");
	};	

};


int main() {
	Item item;	
//	item.name = "coca_cola";

	VendingMachine machine;
	machine.activate();

	
	return 0;
}
