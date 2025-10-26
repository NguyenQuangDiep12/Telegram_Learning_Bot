"""
Handler cho thực hành và LeetCode
"""

import random
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ContextTypes


# Danh sách bài tập LeetCode theo chủ đề
LEETCODE_PROBLEMS = {
    'arrays': [
        {
            'title': 'Two Sum',
            'difficulty': 'Easy',
            'description': 'Tìm hai số trong array có tổng bằng target',
            'example': 'Input: nums = [2,7,11,15], target = 9\nOutput: [0,1]',
            'hint': 'Sử dụng HashMap để lưu số đã duyệt'
        },
        {
            'title': 'Best Time to Buy and Sell Stock',
            'difficulty': 'Easy',
            'description': 'Tìm lợi nhuận tối đa khi mua bán cổ phiếu',
            'example': 'Input: prices = [7,1,5,3,6,4]\nOutput: 5',
            'hint': 'Theo dõi giá nhỏ nhất và lợi nhuận lớn nhất'
        },
        {
            'title': 'Three Sum',
            'difficulty': 'Medium',
            'description': 'Tìm ba số có tổng bằng 0',
            'example': 'Input: nums = [-1,0,1,2,-1,-4]\nOutput: [[-1,-1,2],[-1,0,1]]',
            'hint': 'Sắp xếp và sử dụng two pointers'
        }
    ],
    'strings': [
        {
            'title': 'Valid Anagram',
            'difficulty': 'Easy',
            'description': 'Kiểm tra hai chuỗi có phải anagram',
            'example': 'Input: s = "anagram", t = "nagaram"\nOutput: true',
            'hint': 'Sắp xếp hoặc đếm ký tự'
        },
        {
            'title': 'Longest Substring Without Repeating Characters',
            'difficulty': 'Medium',
            'description': 'Tìm độ dài chuỗi con không lặp',
            'example': 'Input: s = "abcabcbb"\nOutput: 3',
            'hint': 'Sliding window với Set'
        }
    ],
    'dynamic_programming': [
        {
            'title': 'Climbing Stairs',
            'difficulty': 'Easy',
            'description': 'Tính số cách leo cầu thang n bậc',
            'example': 'Input: n = 3\nOutput: 3',
            'hint': 'dp[i] = dp[i-1] + dp[i-2]'
        },
        {
            'title': 'Coin Change',
            'difficulty': 'Medium',
            'description': 'Tìm số tiền xu nhỏ nhất để đạt được amount',
            'example': 'Input: coins = [1,2,5], amount = 11\nOutput: 3',
            'hint': 'DP với dp[i] = min(dp[i], dp[i-coin]+1)'
        },
        {
            'title': 'Longest Common Subsequence',
            'difficulty': 'Medium',
            'description': 'Tìm độ dài chuỗi con chung dài nhất',
            'example': 'Input: text1 = "abcde", text2 = "ace"\nOutput: 3',
            'hint': 'dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]+1 if match)'
        }
    ],
    'binary_search': [
        {
            'title': 'Binary Search',
            'difficulty': 'Easy',
            'description': 'Tìm target trong sorted array',
            'example': 'Input: nums = [-1,0,3,5,9,12], target = 9\nOutput: 4',
            'hint': 'left = 0, right = len-1, while left <= right'
        },
        {
            'title': 'Search in Rotated Sorted Array',
            'difficulty': 'Medium',
            'description': 'Tìm target trong rotated sorted array',
            'example': 'Input: nums = [4,5,6,7,0,1,2], target = 0\nOutput: 4',
            'hint': 'So sánh nums[mid] với nums[left] để tìm pivot'
        }
    ],
    'trees': [
        {
            'title': 'Maximum Depth of Binary Tree',
            'difficulty': 'Easy',
            'description': 'Tìm độ sâu lớn nhất của binary tree',
            'example': 'Input: root = [3,9,20,null,null,15,7]\nOutput: 3',
            'hint': 'DFS: return 1 + max(dfs(left), dfs(right))'
        },
        {
            'title': 'Validate Binary Search Tree',
            'difficulty': 'Medium',
            'description': 'Kiểm tra BST có hợp lệ',
            'example': 'Input: root = [2,1,3]\nOutput: true',
            'hint': 'So sánh với min và max boundary'
        }
    ]
}


async def handle_practice_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Hiển thị menu thực hành"""
    practice_keyboard = [
        [KeyboardButton('Arrays & Strings'), KeyboardButton('Dynamic Programming')],
        [KeyboardButton('Binary Search'), KeyboardButton('Trees & Graphs')],
        [KeyboardButton('Practice C#'), KeyboardButton('Practice JavaScript')],
        [KeyboardButton('🔙 Về Menu Chính')]
    ]
    
    await update.message.reply_text(
        "💻 *MENU THỰC HÀNH*\n\n"
        "Chọn chủ đề bạn muốn luyện tập:\n\n"
        "• Arrays & Strings\n"
        "• Dynamic Programming\n"
        "• Binary Search\n"
        "• Trees & Graphs\n"
        "• Practice C#/JavaScript",
        parse_mode='Markdown',
        reply_markup=ReplyKeyboardMarkup(practice_keyboard, resize_keyboard=True)
    )
    
    context.user_data['awaiting_practice'] = True


async def handle_leetcode_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Xử lý yêu cầu bài tập LeetCode"""
    text = update.message.text
    
    category_map = {
        'Arrays & Strings': 'arrays',
        'Dynamic Programming': 'dynamic_programming',
        'Binary Search': 'binary_search',
        'Trees & Graphs': 'trees'
    }
    
    if text in category_map:
        category = category_map[text]
        problems = LEETCODE_PROBLEMS.get(category, [])
        
        if problems:
            # Chọn bài tập ngẫu nhiên
            problem = random.choice(problems)
            
            response = f"""
💻 *Bài Tập: {problem['title']}*

📊 *Độ Khó:* {problem['difficulty']}

📝 *Mô Tả:*
{problem['description']}

📌 *Ví Dụ:*
```
{problem['example']}
```

💡 *Gợi Ý:*
{problem['hint']}

🔗 Thử solve tại: leetcode.com
"""
            
            # Keyboard để request another
            practice_keyboard = [
                [KeyboardButton('🔁 Bài Tập Khác'), KeyboardButton('🔙 Về Menu Chính')]
            ]
            
            await update.message.reply_text(
                response,
                parse_mode='Markdown',
                reply_markup=ReplyKeyboardMarkup(practice_keyboard, resize_keyboard=True)
            )
        else:
            await update.message.reply_text("❌ Chưa có bài tập cho chủ đề này!")
    
    elif text == '🔁 Bài Tập Khác':
        await handle_practice_menu(update, context)
    
    elif text in ['Practice C#', 'Practice JavaScript']:
        language = text.replace('Practice ', '')
        practice_code = get_practice_code(language)
        
        keyboard = [
            [KeyboardButton('💻 Yêu Cầu Bài Tập Khác'), KeyboardButton('🔙 Về Menu Chính')]
        ]
        
        await update.message.reply_text(
            practice_code,
            parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        )


def get_practice_code(language: str) -> str:
    """Trả về bài tập code theo ngôn ngữ"""
    if language == 'C#':
        return """
💻 *Bài Tập C# - Thực Hành*

🔸 *Bài 1: Implement LINQ Where*
```csharp
public static IEnumerable<T> MyWhere<T>(
    this IEnumerable<T> source, 
    Func<T, bool> predicate) {
    // Your code here
}
```

🔸 *Bài 2: Async File Reader*
```csharp
public async Task<string> ReadFileAsync(string path) {
    // Read file asynchronously
}
```

🔸 *Bài 3: Generic Repository Pattern*
```csharp
public interface IRepository<T> where T : class {
    Task<IEnumerable<T>> GetAllAsync();
    Task<T> GetByIdAsync(int id);
    Task<T> AddAsync(T entity);
}
```

💡 Viết implementation cho các bài trên!
"""
    else:  # JavaScript
        return """
💻 *Bài Tập JavaScript - Thực Hành*

🔸 *Bài 1: Implement Array Methods*
```javascript
Array.prototype.myMap = function(callback) {
    // Your implementation
}

Array.prototype.myFilter = function(callback) {
    // Your implementation
}
```

🔸 *Bài 2: Async Data Fetching*
```javascript
async function fetchMultiple(urls) {
    // Fetch multiple URLs concurrently
    // Return results in order
}
```

🔸 *Bài 3: Debounce Function*
```javascript
function debounce(func, delay) {
    // Return debounced version of func
}
```

💡 Implement các function trên!
"""
