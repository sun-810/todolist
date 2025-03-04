from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
todos = []  # 메모리에 To-Do 리스트 저장 (나중에 DB로 확장 가능)

# 홈페이지 렌더링
@app.route('/')
def index():
    return render_template('index.html', todos=todos)

# 모든 투두 가져오기
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# 투두 추가
@app.route('/todos', methods=['POST'])
def add_todo():
    todo = request.json.get('task')
    if todo:
        todos.append(todo)
        return jsonify({'message': 'Todo added successfully'}), 201
    return jsonify({'error': 'Invalid todo'}), 400

# 투두 삭제
@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    if 0 <= todo_id < len(todos):
        deleted_todo = todos.pop(todo_id)
        return jsonify({'message': 'Todo deleted', 'deleted': deleted_todo}), 200
    return jsonify({'error': 'Invalid todo ID'}), 404

if __name__ == '__main__':
    app.run(debug=True)
