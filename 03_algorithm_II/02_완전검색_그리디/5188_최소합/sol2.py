import sys

sys.stdin = open('input.txt')

'''
모든 경우에서 오른쪽, 아래 방향으로만 조사가 가능하다.
델타 탐색
'''
dx = [0, 1]
dy = [1, 0]


def search(x, y):  # x, y 부터 조사 시작.
    # 누적값인데 왜 arr[x][y]의 값으로 초기화 ?
    # 값을  들고 이동하기 때문에 상관x
    stack = [[x, y, arr[x][y]]]  # 해당 지점 도달까지 들었던 누적값
    while stack:  # 모든 조사 대상 조사 완료 할 때 까지
        x, y, cnt = stack.pop()
        for k in range(2):  # 우, 하 양방향 조사
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < N and ny < N:  # 범위를 벗어나면 안된다.
                '''
                    내가 [nx][ny] 번째에 도달하려고 할때 드는 누적값
                    이번 조사에서 쌓아온 누적값이
                    이전번 누군가가 쌓아온  누적값보다 적은 경우에만
                    이동할 수 있도록 코드를 작성해야한다.
                '''
                if visited[nx][ny] > cnt + arr[nx][ny]:
                    visited[nx][ny] = cnt + arr[nx][ny]
                    for v in visited:
                        print(v)
                    print()
                    stack.append((nx, ny, cnt + arr[nx][ny]))


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 방문 표시 리스트
    # N * N의 2차원 리스트로 arr와 완전히 동일한 크기로 만든다.
    '''
        나중에는, 이곳에 특정 좌표에 도달하는데 드는 누적값을 기록
        그  누적값들은, 최솟값으로 갱신할 것이다.
        그럼, 첫 비교 대상은 충분히 큰 값이어야한다.
    '''
    visited = [[N * N * 10] * N for _ in range(N)]
    for a in arr:
        print(a)

    print(f'#{tc}')