#include<bits/stdc++.h>
using namespace std;
////////////////////////////////////////////////////////////////
/*
    The idea I am using is that bringing all the 1's together is same as 
    getting all the zeros away. The question says that all the 1's are 
    together but it does not say that the zeros have to be together too.
    Thus the question is reduced to moving the zeros towards the ends in the
    least number of moves which eventually gets the 1's together.
    Swapping a 0 and another adjacent 0 is a useless move. Thus it is enough 
    to count the number of 0 and 1 swaps required. So I am counting the number 
    of 1's on each side of a zero. 
*/
void solve()
{
    int n;
    cin >> n;

    int arr[n];
    int tot = 0; // number of 1's
    map<int,int> m; // index of each 0 mapped with the no of 1's on its left.
    vector<int> v; // Stores the index of each zero

    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
        if(arr[i] == 1)
        {
            tot += 1;
        }
        else
        {
            // Till now the number of 1's encountered is stored in tot. 
            // Thus this represents the number of 1's to the left of the 0
            m[i] = tot;
            v.push_back(i); // to store the index
        }
    }

    int ans = 0; 
    for(int c: v)
    {
        ans += min(m[c],tot - m[c]);
        // tot - m[c] is the number of 1's on the right
    }
    cout << ans << "\n";
}

//////////////////////////////////////////////////////////////
int32_t main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    // int t;
    // cin>>t;
    
    // while(t--)
    solve();

    return 0;
}