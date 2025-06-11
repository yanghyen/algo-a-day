# List(배열)

## 개념
- 가장 자유로운 선형 자료구조
- 순서를 가진 항목들의 모임
- 중복 허용
- 구현에 따라 크기가 동적일 수도, 정적일 수도 있음
- Stack, Queue, Deque와의 차이점: 자료의 접근 위치, 리스트는 임의의 위치에서도 항목의 삽입과 삭제 가능

## 구조
1. 배열 구조(array)
- 구현이 간단
- 항목 접근(인덱싱, 슬라이싱): O(1)
- 삽입, 삭제 비효율적 (맨 뒤에서의 삽입/삭제는 O(1), 나머지는 O(n))
- Python, Java(배열, 연결 선택 가능)
- 항목의 크기 제한

2. 연결된 구조(linked list)
- 구현이 복잡: 시작 항목이 지정되고, 다른 항목과 링크로 연결됨
- 항목 접근: O(n)
- 삽입, 삭제 효율적
- 크기 제한 없음

## Python List
- 동적 배열로 구현: 필요한 양보다 넉넉한 크기의 메모리 사용
- Python 내 List는 ```PyListObject```라는 객체
    - ob_item은 실제로 데이터를 저장하는 메모리 블록을 가리킴
    ```C
    typedef struct {
        PyObject_VAR_HEAD
        PyObject **ob_item;  // 실제 데이터를 담는 배열 (포인터 배열)
        Py_ssize_t allocated;  // 현재 할당된 메모리 크기 (capacity)
    } PyListObject;
    ```
- 용량을 초과하면 어떻게 처리하는가?
    - capacity doubling 전략: 초기 메모리를 넉넉히 할당해두고, 요소가 늘어나면 용량(capacity)을 자동으로 늘리는 방식
    1. 용량이 넘치기 전
    - PyListObject는 메모리에 존재하고, 그 안에 있는 ob_item 포인터는 [a, b, c, d] 같은 배열을 가리킴
    2. append() 하다가 용량 초과
    - 새로운 더 큰 메모리 블록을 만듦 (예: [a, b, c, d, e, _, _, _])
    - 기존 데이터 [a, b, c, d]를 새 배열로 복사 그리고 ob_item 포인터를 새 배열을 가리키도록 교체
    - allocated 값도 새로운 용량으로 갱신
    - 이 과정에서 PyListObject 자체는 그대로이고,
    - 오직 내부의 ob_item 포인터만 바뀐 것