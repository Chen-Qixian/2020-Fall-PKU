#include <bits/stdc++.h>
using namespace std;

const int inf=0x3f3f3f3f;
const int Max_v=2e4+10;

struct edge{ //用于表示边的结构体(终点，容量，反向边）
    int to,cap,rev;
    edge(int t,int c,int r):to(t),cap(c),rev(r){}
};
vector<edge>G[Max_v]; //图的邻接表表示
int level[Max_v]; //顶点到源点的距离标号
int iter[Max_v];  //当前弧，在其之前的边已经没有用了

//向图中增加一条从from到to的容量为cap的边
void add_edge(int from,int to,int cap){
    G[from].push_back(edge(to,cap,G[to].size()));
    G[to].push_back(edge(from,0,G[from].size()-1));
}

//通过BFS计算从原点出发的距离标号
void bfs(int s){
    memset(level,-1,sizeof(level));
    queue<int>que;
    que.push(s);
    level[s]=0;
    while(!que.empty()){
        int v=que.front();que.pop();
        for(int i=0;i<G[v].size();i++){
            edge &e=G[v][i];
            if(e.cap>0&&level[e.to]<0){
                level[e.to]=level[v]+1;
                que.push(e.to);
            }
        }
    }
}

//通过dfs寻找增广路
int dfs(int v,int t,int f){
    if(v==t)return f;
    for(int &i=iter[v];i<G[v].size();i++){
        edge &e=G[v][i];
        if(e.cap>0&&level[v]<level[e.to]){
            int d=dfs(e.to,t,min(f,e.cap));
            if(d>0){
                e.cap-=d;
                G[e.to][e.rev].cap+=d;
                return d;
            }
        }
    }
    return 0;
}

//求解从s到t的最大流
int dinic(int s,int t){
    int flow=0;
    for(;;){
        bfs(s);
        if(level[t]<0)return flow;
        memset(iter,0,sizeof(iter));
        int f;
        while((f=dfs(s,t,inf))>0){
            flow+=f;
        }
    }
}
