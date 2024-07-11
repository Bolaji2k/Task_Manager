from flask import jsonify, request, after_this_request, redirect
from .models import Task, db
from datetime import datetime, date
from flask_cors import CORS,cross_origin

def create_view(app):
    @app.route('/')
    def index():
        return jsonify({
            'name': 'Johnpeter',
            'sex': 'Male'
        })
    @app.route('/api/v1/task/<id>', methods = ['DELETE','GET','PUT'])
    def get_task(id):
        if request.method == 'GET':
            try: 
                task = int(id)
                task = Task.query.get(task)
            except:
                task = Task.query.filter_by(title=id).first()


            if task:
                return jsonify(task.serialize())
            else:
                return jsonify ({'error': 'No task is found'})
        if request.method == 'DELETE':
            try: 
                task = int(id)
                task = Task.query.get(task)
            except:
                task = Task.query.filter_by(title=id).first()

            if task:
                db.session.delete(task)
                db.session.commit()
                return jsonify ({'status': 'successful'})
            else:
                return jsonify ({'status': 'unsuccessful'})
            
        if request.method == 'PUT':
            
            try: 
                task = int(id)
                task = Task.query.get(task)
            except:
                task = Task.query.filter_by(title=id).first()

            if task:
                form = request.get_json()

                if request.is_json: 
                    title = form.get('title')
                    description = form.get('description')
                    status = form.get('status')
                    created_date = form.get('created_date')
                    created_date = datetime.fromisoformat(created_date).date()
                    completed_date = form.get('completed_date')
                    due_date = form.get('due_date')

                    if completed_date != '':
                        completed_date = datetime.fromisoformat(completed_date).date()
                    if due_date != '':
                        due_date = datetime.fromisoformat(due_date).date()

                    if status == False:
                        completed_date = None


                        
                    
                    task.title = title
                    task.description = description
                    task.status = status
                    task.created_date = created_date
                    task.completed_date = completed_date
                    task.due_date = due_date

                    db.session.add(task)
                    db.session.commit()
                

                return jsonify(task.serialize())
            else:
                return jsonify ({'status': 'unsuccessful'})


        
        
        
    @app.route('/api/v1/tasks', methods = ['POST', 'GET'])
    def get_all_task():
        # @after_this_request
        # def add_header(response):
        #     response.headers['Access-Control-Allow-Origin'] = '*'
        #     return response
        if request.method == 'GET':
         tasks = Task.query.all()

         if tasks:
            data = {'task': [task.serialize() for task in tasks]}
         else:
            data = {'task': 'You don\'t have any task'}

        if request.method == 'POST':
            form = request.get_json()

            if request.is_json  :
                title = form.get('title')
                description = form.get('description')
                status = form.get('status')
                created_date = date.today() 
                due_date = form.get('due_date')
                due_date = datetime.fromisoformat(due_date).date()



                task = Task(
                    title=title,
                    description = description,
                    status = status,
                    created_date = created_date,     
                    due_date = due_date     
                )

                try :
                    db.session.add(task)
                    db.session.commit()
                except Exception as e:
                    db.session.rollback()
                    return jsonify ({'error': str(e)})


                return jsonify(task.serialize())
            else: 
                return jsonify ({'error': 'Your form is empty'})
                
    

        return jsonify(data)

      