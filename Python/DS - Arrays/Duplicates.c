//Array from a new array
//Selecting of those numbers which occur at least more than once
#include<stdio.h>
int main()
{
	int n,i,j;
	printf("Enter the no of elements=");
	scanf("%d",&n);
	int arr[n];
	for(i=0;i<n;i++)
		scanf("%d",&arr[i]);
	for(i=0;i<=n-2;i++)
	{
		for(j=i+1;j<n;j++)
		{
			if(arr[i]==arr[j])
			{
				arr[j]=-1;
				printf("%d",arr[i]);
			}
		}
	}
	return 0;
}