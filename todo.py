# Main 함수 구현 메뉴별 기본 기능 설계
# 메뉴별 입력값 및 Todo 기초 툴 구현
import json
import os # 파이썬을 이용해서 시스템 내부에 접근이 가능하다

task_file = 'tasks.json'

def load_task():
    if os.path.exists(task_file): #파일이 있는 경우
        with open(task_file, 'r', encoding='utf-8') as file: #file => open(task_file, 'r', encoding='utf-8')
            return json.load(file) #json.load()
    return {}
        
def save_task(tasks): #add_task를 통해 전달받은 해야할 일을 파일에 저장하는 기능
    with open(task_file, 'w', encoding='utf-8') as file: #file => open(TASK_FILE, 'w', encoding='utf-8')
        json.dump(tasks, file, indent=4, ensure_ascii=False)
        
def add_task(task_name): # 할 일 추가
    tasks = load_task() # 파일이 있다면 가져와
    task = {'name' : "파이썬 공부하기", 'completed' : False} #파이썬 공부하기에 대한 데이터가 들어갔어
    tasks.append(task)
    save_task(tasks)

def view_task(): # 할 일 목록 보기
    pass

def complete_task(task_number): # 할 일 완료
    pass

def delete_task(task_number): # 할 일 삭제 -> 함수????? / tasks.insert() / len()
    tasks = load_task()
    if 1 <= task_number <= len(tasks): # 1<task_number<1 / tasks => [{}]
        delete_tsk = tasks.pop(task_number-1) #index 값 넣어야해요 / pop()통해서 삭제 및 변환이 되고 삭제가 된 데이터가 delete_tsk에 들어간다 -> [{}] -> []
        save_task(tasks) # tasks.pop(task_number-1) => [{"name": "파이썬 공부하기", "completed": true}] => [] => tasks
        print(f"할 일 : '{delete_tsk['name']}'이(가) 사라졌습니다.")
    else:
        print("유효하지 않은 작업 번호입니다. 다시 확인해주세요")

def show_menu(): #메뉴를 보여주는 함수
    print("작업 관리 어플리케이션")
    print("1. 할 일 추가")
    print("2. 할 일 목록보기")
    print("3. 할 일 완료")
    print("4. 할 일 삭제")
    print("5. 종료")
    
def main():
    while True:
        show_menu()
        choice = input("원하는 작업을 선택해주세요 (1~5): ") # 1
        
        if choice == '1':
            task_name = input("추가할 작업을 입력해주세요") # 파이썬 공부하기
            add_task(task_name)
        elif choice == '2':
            view_task()
        elif choice == '3':
            task_number = int(input("완료를 원하는 작업의 번호를 입력해주세요."))
            complete_task(task_number)           
        elif choice == '4':
            task_number = int(input("삭제를 원하는 작업의 번호를 입력해주세요."))
            delete_task(task_number)
        elif choice == '5':
            print("시스템을 종료합니다.")
            break
        else:
            print("잘못 입력하셨습니다. 1번부터 5번까지의 기능 중 하나를 선택해주세요.")
            
main()