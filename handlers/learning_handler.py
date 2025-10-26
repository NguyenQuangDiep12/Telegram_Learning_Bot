"""
Handler cho việc học lý thuyết và quiz
"""

from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ContextTypes


# Nội dung học tập cho từng chủ đề
LEARNING_CONTENT = {
    'C# & .NET': """
📚 *C# & .NET - Lý Thuyết*

🔸 *1. C# Basics:*
   • Type-safe, object-oriented programming
   • Garbage collection
   • Nullable types: int? x = null;
   • Pattern matching

🔸 *2. OOP Concepts:*
   • Encapsulation, Inheritance, Polymorphism
   • Abstract classes vs Interfaces
   • sealed, virtual, override keywords

🔸 *3. LINQ:*
   ```csharp
   var numbers = new[] {1, 2, 3, 4, 5};
   var even = numbers.Where(n => n % 2 == 0);
   var sum = numbers.Sum();
   ```

🔸 *4. Async/Await:*
   ```csharp
   public async Task<string> GetDataAsync() {
       var result = await httpClient.GetAsync(url);
       return await result.Content.ReadAsStringAsync();
   }
   ```

🔸 *5. Entity Framework:*
   • DbContext & DbSet
   • Migration & Code First
   • Linq queries to SQL

🔸 *6. ASP.NET Core:*
   • Middleware pipeline
   • Dependency Injection
   • Controllers & Actions
   • Routing & Filters
""",
    
    'JavaScript': """
📚 *JavaScript - Lý Thuyết*

🔸 *1. ES6+ Features:*
   ```javascript
   // Arrow functions
   const sum = (a, b) => a + b;
   
   // Destructuring
   const [first, second] = array;
   const {name, age} = user;
   
   // Spread operator
   const newArr = [...arr1, ...arr2];
   ```

🔸 *2. Async/Await & Promises:*
   ```javascript
   // Promise
   fetch(url)
     .then(response => response.json())
     .then(data => console.log(data));
   
   // Async/Await
   const getData = async () => {
     const response = await fetch(url);
     return await response.json();
   };
   ```

🔸 *3. Closures:*
   ```javascript
   function createCounter() {
     let count = 0;
     return function() {
       return ++count;
     };
   }
   ```

🔸 *4. Scope & Hoisting:*
   • var, let, const differences
   • Temporal Dead Zone
   • Function vs Block scope

🔸 *5. Modules:*
   ```javascript
   // Export
   export const name = "John";
   export function greet() { }
   
   // Import
   import { name, greet } from './module';
   ```
""",
    
    'TypeScript': """
📚 *TypeScript - Lý Thuyết*

🔸 *1. Type System:*
   ```typescript
   // Basic types
   let name: string = "John";
   let age: number = 25;
   let isActive: boolean = true;
   
   // Arrays
   let numbers: number[] = [1, 2, 3];
   let words: Array<string> = ["a", "b"];
   ```

🔸 *2. Interfaces & Types:*
   ```typescript
   interface User {
     name: string;
     age: number;
     email?: string; // Optional
   }
   
   type Status = 'active' | 'inactive';
   ```

🔸 *3. Generics:*
   ```typescript
   function identity<T>(arg: T): T {
     return arg;
   }
   
   const result = identity<string>("hello");
   ```

🔸 *4. Advanced Types:*
   ```typescript
   // Union types
   type ID = string | number;
   
   // Intersection types
   type SuperUser = User & Admin;
   
   // Type guards
   if (typeof x === 'string') { }
   ```

🔸 *5. Decorators:*
   ```typescript
   @Component({
     selector: 'app-root',
     template: '<h1>Hello</h1>'
   })
   class AppComponent { }
   ```
""",
    
    'ReactJS': """
📚 *ReactJS - Lý Thuyết*

🔸 *1. Components:*
   ```javascript
   function Welcome(props) {
     return <h1>Hello, {props.name}</h1>;
   }
   
   // Or Class Component
   class Welcome extends React.Component {
     render() {
       return <h1>Hello, {this.props.name}</h1>;
     }
   }
   ```

🔸 *2. Hooks - useState:*
   ```javascript
   import { useState } from 'react';
   
   function Counter() {
     const [count, setCount] = useState(0);
     return <button onClick={() => setCount(count + 1)}>{count}</button>;
   }
   ```

🔸 *3. Hooks - useEffect:*
   ```javascript
   import { useEffect, useState } from 'react';
   
   function DataLoader() {
     const [data, setData] = useState(null);
     
     useEffect(() => {
       fetch(url).then(res => setData(res));
     }, []); // Empty deps = run once
     
     return <div>{data}</div>;
   }
   ```

🔸 *4. Context API:*
   ```javascript
   const ThemeContext = createContext();
   
   function App() {
     return (
       <ThemeContext.Provider value="dark">
         <ThemedButton />
       </ThemeContext.Provider>
     );
   }
   ```

🔸 *5. State Management:*
   • State lifting
   • Prop drilling vs Context
   • Redux, Zustand, Jotai
   • useReducer for complex state

🔸 *6. Performance:*
   • useMemo, useCallback
   • React.memo
   • Code splitting & lazy loading
"""
}


# Câu hỏi quiz
QUIZ_QUESTIONS = {
    'C#': [
        {
            'question': 'C# là ngôn ngữ gì?',
            'options': ['Compiled', 'Interpreted', 'Both', 'None'],
            'correct': 0,
            'explanation': 'C# được compiled thành Intermediate Language (IL)'
        },
        {
            'question': 'Từ khóa nào để kế thừa class?',
            'options': ['extends', 'inherits', ':', 'implements'],
            'correct': 2,
            'explanation': 'C# sử dụng : để kế thừa class'
        },
        {
            'question': 'LINQ là viết tắt của gì?',
            'options': ['Language Integrated Query', 'Lazy Interactive Query', 'Large Input Query', 'None'],
            'correct': 0,
            'explanation': 'LINQ = Language Integrated Query'
        }
    ],
    'JavaScript': [
        {
            'question': 'var, let, const khác nhau như thế nào?',
            'options': ['Same', 'Scope khác nhau', 'Hoisting khác nhau', 'All above'],
            'correct': 3,
            'explanation': 'var - function scope, hoisted; let/const - block scope, TDZ'
        },
        {
            'question': 'Promise có mấy trạng thái?',
            'options': ['2', '3', '4', '1'],
            'correct': 1,
            'explanation': 'Promise có 3 trạng thái: pending, fulfilled, rejected'
        },
        {
            'question': 'Closure là gì?',
            'options': ['Function + Variables', 'Just function', 'Async function', 'None'],
            'correct': 0,
            'explanation': 'Closure = Function có thể truy cập biến từ scope ngoài'
        }
    ]
}


async def handle_learning_topics(update: Update, context: ContextTypes.DEFAULT_TYPE, topic: str):
    """Xử lý khi người dùng chọn chủ đề học"""
    if topic in LEARNING_CONTENT:
        content = LEARNING_CONTENT[topic]
        
        # Tạo menu quay lại
        back_keyboard = [
            [KeyboardButton('🔙 Về Menu Chính')]
        ]
        
        await update.message.reply_text(
            content,
            parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup(back_keyboard, resize_keyboard=True)
        )
    else:
        await update.message.reply_text("❌ Chủ đề không tìm thấy!")


async def handle_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE, quiz_type: str):
    """Xử lý quiz"""
    # Extract topic từ "Quiz C#" -> "C#"
    topic = quiz_type.replace('Quiz ', '').strip()
    
    if topic in QUIZ_QUESTIONS:
        # Lấy câu hỏi ngẫu nhiên
        import random
        questions = QUIZ_QUESTIONS[topic]
        selected_question = random.choice(questions)
        
        # Lưu vào user_data để theo dõi
        context.user_data['current_quiz'] = {
            'topic': topic,
            'question': selected_question['question'],
            'correct': selected_question['correct'],
            'options': selected_question['options'],
            'explanation': selected_question['explanation']
        }
        
        # Tạo options keyboard
        options_buttons = [[KeyboardButton(f"📝 {opt}")] for opt in selected_question['options']]
        options_buttons.append([KeyboardButton('🔙 Về Menu Chính')])
        
        await update.message.reply_text(
            f"📊 *Quiz {topic}*\n\n{selected_question['question']}\n\n"
            f"Chọn câu trả lời:",
            parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup(options_buttons, resize_keyboard=True, one_time_keyboard=True)
        )
    else:
        await update.message.reply_text("❌ Quiz chưa được hỗ trợ!")


def get_quiz_content():
    """Trả về nội dung quiz"""
    return QUIZ_QUESTIONS
