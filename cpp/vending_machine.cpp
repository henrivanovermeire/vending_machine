#include <stdio.h>

struct Item {
	char name[128];
	int price;
};

struct VendingMachine{
	void activate() {
		printf("Vending machine activated!\n");
		while (true) {
			printf("running...\n");
		}
	};	

};


int main() {
	Item item;	
//	item.name = "coca_cola";
	item.price = 1;
	VendingMachine machine;
	machine.activate();

	
	return 0;
}
