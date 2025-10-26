"""
Handler cho AI Assistant
"""

import os
from telegram import Update
from telegram.ext import ContextTypes
from config import GEMINI_API_KEY, OPENAI_API_KEY


async def handle_ai_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Xử lý câu hỏi AI"""
    question = update.message.text
    
    # Nếu không có API key, sử dụng rule-based responses
    if not GEMINI_API_KEY and not OPENAI_API_KEY:
        response = await get_rule_based_response(question)
    else:
        # Sử dụng AI API
        try:
            if GEMINI_API_KEY:
                response = await get_gemini_response(question)
            elif OPENAI_API_KEY:
                response = await get_openai_response(question)
            else:
                response = await get_rule_based_response(question)
        except Exception as e:
            print(f"AI Error: {e}")
            response = await get_rule_based_response(question)
    
    await update.message.reply_text(response, parse_mode='Markdown')


async def get_rule_based_response(question: str) -> str:
    """Trả về câu trả lời dựa trên keywords (fallback khi không có AI API)"""
    question_lower = question.lower()
    
    # C# .NET keywords
    if any(kw in question_lower for kw in ['async', 'await', 'async/await']):
        return """
🔹 *Async/Await trong C#:*

✅ Async/await giúp code chạy bất đồng bộ mà không block thread.

```csharp
public async Task<string> GetDataAsync() {
    // Method này sẽ chạy async
    var response = await httpClient.GetAsync(url);
    var content = await response.Content.ReadAsStringAsync();
    return content;
}
```

📌 *Key Points:*
• async keyword làm method return Task hoặc Task<T>
• await chờ async operation hoàn thành
• Không block UI thread
• Giúp tăng hiệu suất ứng dụng
"""
    
    elif any(kw in question_lower for kw in ['linq', 'lambda', 'query']):
        return """
🔹 *LINQ trong C#:*

✅ Language Integrated Query - truy vấn dữ liệu trực tiếp trong C#.

```csharp
var numbers = new[] {1, 2, 3, 4, 5, 6};

// Query syntax
var evens = from n in numbers 
           where n % 2 == 0 
           select n;

// Method syntax (thường dùng hơn)
var evens = numbers.Where(n => n % 2 == 0);

// More examples
var sum = numbers.Sum();
var max = numbers.Max();
var avg = numbers.Average();
var grouped = numbers.GroupBy(n => n % 2);
```

📌 *Common Methods:*
• Where(), Select(), OrderBy()
• First(), Any(), All()
• Sum(), Max(), Min(), Average()
"""
    
    elif any(kw in question_lower for kw in ['react', 'hooks']):
        return """
🔹 *React Hooks:*

✅ Hooks cho phép dùng state và features khác trong function components.

```javascript
import { useState, useEffect } from 'react';

function MyComponent() {
    // useState - state management
    const [count, setCount] = useState(0);
    
    // useEffect - side effects
    useEffect(() => {
        document.title = `Count: ${count}`;
        return () => {
            // Cleanup function
        };
    }, [count]); // Dependencies
    
    return (
        <button onClick={() => setCount(count + 1)}>
            Count: {count}
        </button>
    );
}
```

📌 *Common Hooks:*
• useState - state
• useEffect - side effects
• useContext - context API
• useMemo, useCallback - performance
"""
    
    elif any(kw in question_lower for kw in ['javascript', 'js', 'es6']):
        return """
🔹 *JavaScript ES6+:*

✅ Các tính năng mới từ ES6 trở đi:

```javascript
// Arrow Functions
const add = (a, b) => a + b;

// Destructuring
const [first, second] = array;
const {name, age} = user;

// Spread Operator
const newArr = [...arr1, ...arr2];
const newObj = {...obj1, ...obj2};

// Template Literals
const message = `Hello ${name}, you are ${age}`;

// Modules
export const myFunction = () => {};
import { myFunction } from './module';

// Promises & Async/Await
const getData = async () => {
    const response = await fetch(url);
    return await response.json();
};
```
"""
    
    elif any(kw in question_lower for kw in ['typescript', 'ts']):
        return """
🔹 *TypeScript Basics:*

✅ TypeScript = JavaScript + Static Types

```typescript
// Type annotations
let name: string = "John";
let age: number = 25;
let isActive: boolean = true;

// Interfaces
interface User {
    name: string;
    age: number;
    email?: string; // Optional
}

// Type inference
const user: User = {
    name: "John",
    age: 25
};

// Generics
function identity<T>(arg: T): T {
    return arg;
}

// Classes with types
class Person {
    constructor(public name: string, public age: number) {}
}
```

📌 *Benefits:*
• Type safety
• Better IDE support
• Compile-time error checking
"""
    
    elif any(kw in question_lower for kw in ['closure', 'scoping']):
        return """
🔹 *JavaScript Closures:*

✅ Closure = Function có thể truy cập biến từ scope ngoài

```javascript
function outerFunction() {
    const outerVariable = 'I am outside!';
    
    function innerFunction() {
        console.log(outerVariable); // Access outer scope
    }
    
    return innerFunction;
}

const myFunc = outerFunction();
myFunc(); // "I am outside!"

// Practical example
function createCounter() {
    let count = 0;
    return function() {
        return ++count; // Access to count
    };
}

const counter = createCounter();
console.log(counter()); // 1
console.log(counter()); // 2
```

📌 *Use Cases:*
• Data privacy / Encapsulation
• Function factories
• Module pattern
"""
    
    elif any(kw in question_lower for kw in ['promise', 'async']):
        return """
🔹 *Promises & Async/Await:*

```javascript
// Promise
const promise = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve('Success!');
        // or reject('Error');
    }, 1000);
});

promise
    .then(result => console.log(result))
    .catch(error => console.log(error));

// Async/Await (modern way)
async function fetchData() {
    try {
        const response = await fetch(url);
        const data = await response.json();
        return data;
    } catch (error) {
        console.error(error);
    }
}

// Parallel requests
async function fetchMultiple() {
    const [data1, data2] = await Promise.all([
        fetch(url1),
        fetch(url2)
    ]);
}
```
"""
    
    else:
        return """
🤖 *AI Assistant:*

💡 Tôi là trợ lý học tập thông minh cho C#, .NET, JavaScript, TypeScript, React!

❓ *Bạn có thể hỏi về:*
• Cú pháp và cách sử dụng các tính năng
• Best practices và patterns
• Debugging và troubleshooting
• So sánh giữa các công nghệ
• Hướng dẫn luyện tập LeetCode

📝 *Tip:* Hỏi cụ thể hơn để nhận câu trả lời chi tiết!

Ví dụ:
• "Giải thích async/await trong C#"
• "Sự khác biệt giữa useState và useReducer"
• "Cách implement debounce function"
"""
    
    return response


async def get_gemini_response(question: str) -> str:
    """Sử dụng Google Gemini API"""
    try:
        import google.generativeai as genai
        
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-pro')
        
        prompt = f"""
Bạn là trợ lý học lập trình chuyên nghiệp.
Trả lời câu hỏi về C#, .NET, JavaScript, TypeScript, React, LeetCode.

Câu hỏi: {question}

Trả lời ngắn gọn, có code examples, format markdown.
"""
        
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Gemini error: {e}")
        return await get_rule_based_response(question)


async def get_openai_response(question: str) -> str:
    """Sử dụng OpenAI GPT API"""
    try:
        from openai import OpenAI
        
        client = OpenAI(api_key=OPENAI_API_KEY)
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful coding tutor for C#, .NET, JavaScript, TypeScript, React, and LeetCode."},
                {"role": "user", "content": question}
            ],
            max_tokens=500
        )
        
        return response.choices[0].message.content
    except Exception as e:
        print(f"OpenAI error: {e}")
        return await get_rule_based_response(question)
