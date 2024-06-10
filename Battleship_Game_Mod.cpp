#include <iostream>
#include <cstdlib>
#include <ctime>
#include <stdlib.h>
using namespace std;

int main(){
	char repeat;
	
	cout << "     Welcome to BATTLESHIP !\n";
	cin.get();
	cout << "Try to enter correct coordinates of the 5x5 matrix for successful attack.\n\n";

	do{
		srand ( (unsigned int)(time(0)) );
	
		bool ship_grid[5][5];
		for (int i=0; i<5;i++){
			for (int j=0; j<5; j++){
				ship_grid[i][j] = 0;
			}
		}
		
		int i, j, k=0;
		while ( k<5) {
			i = 5*(rand()/(float)RAND_MAX);
			j = 5*(rand()/(float)RAND_MAX);
			if (ship_grid[i][j] != 1){
				ship_grid[i][j] = true;
				k++;
			}
		}
		
		int ship_grid_0[5][5];
		for (int i=0; i<5;i++){
			for (int j=0; j<5; j++){
				ship_grid_0[i][j] = ship_grid[i][j];
			}
		}
		
		int ship_grid_1[5][5];
		for (int i=0; i<5;i++){
			for (int j=0; j<5; j++){
				ship_grid_1[i][j] = 0;
			}
		}
		
		for (int i=0; i<5; i++){
			cout << "	";
			for (int j=0; j<5; j++){
				cout << " - " ;
			}
			cout << endl;;
		}
		cout << "\nYour have 10 chances. For each hit, you get +1 chance.\n";
		cin.get();
		
		
		int hit=0;
		int chance=10;
		int turn=0;
		int x,y;
		
		while(chance!=0 && hit!=5){
			cout << "	 Ship left : " << 5-hit << endl;
			cout << "	 Chances left : " << chance << endl;
			cout << "\nEnter coordinates for attack ( row column ) :  ";
			cin >> x >> y;
			cout << endl;
	
			if ( x>5 || y>5){
				cout << "      Invalid coordinates !\n" << endl;
			}
			else{
				if(ship_grid_0[x-1][y-1]==1){
					cout << "	     HIT !!\n" << endl;
					
					hit++;
					chance++;
					ship_grid_0[x-1][y-1] = 2;
					ship_grid_1[x-1][y-1] = 1;
				}
				else if(ship_grid_0[x-1][y-1]==0){
					cout << "	     MISS!\n" << endl;
					
					ship_grid_0[x-1][y-1] = 2;					
					ship_grid_1[x-1][y-1] = 2;
				}
				else {
					cout << "	Already checked.\n" << endl;
					chance++;
				}
				chance--;
				turn++;
			}
	
			for (int i=0; i<5; i++){
				cout << "	";
				for (int j=0; j<5; j++){
					if(ship_grid_1[i][j]==2){
						cout << " 0 " ;
					}
					else if(ship_grid_1[i][j]==1){
						cout << " X ";
					}
					else {
						cout << " - ";
					}
				}
				cout << endl;
			}
			cout << endl;
		}
		
		if (hit==5) {
			cout << "	VICTORY !\n";
			cout << "	You have 0 ships left !\n";
			cout << "	You won in " << turn << " number of turns !\n" << endl;
		}
		else {
			cout << "	SORRY ! YOU LOST !\n";
			cout << "	Location of ships were : \n\n";
			for (int i=0; i<5; i++){
				cout << "	";
				for (int j=0; j<5; j++){
					if(ship_grid[i][j]==1){
						cout << " X " ;
					}
					else{
						cout << " - ";
					}	
				}
				cout << endl;
			}
		
		}
		cout << endl;
		
		cout << "Do you want to try again ? (y/n) ";
		cin >> repeat;
		
		cout << endl;
		cout << "---------------------------------------------------\n";
		system("CLS");
	}
	while ( repeat == 'y' || repeat == 'Y');
	
	cout << "Thank you for playing !!\n" << endl;
	cin.get();
	cout << "--------------------- Credits ---------------------\n";
	cout << "                    Akshay Anil\n" << endl;;
	cout << "---------------------------------------------------\n";
	
	system ("pause");
	return 0;
}
