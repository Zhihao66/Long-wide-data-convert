/**
 * 数据格式转换工具 - 核心逻辑
 * Data Format Converter - Core Logic
 */

// ==================== 辅助函数 ====================

// 记录最后一次检测到的分隔符（用于下载后缀等）
let lastDetectedDelimiter = ',';


/**
 * CSV 字符串转 JSON 数组
 */
function csvToArray(csvString) {
    // 支持 CSV（逗号分隔）和 TSV（制表符分隔）
    // 兼容用户粘贴时把 "\t"（反斜杠加 t）当作文本的情况：把它们转换为真实的制表符
    let normalized = csvString.replace(/\\t/g, '\t');
    // 兼容 Windows 换行 \r\n
    const rawLines = normalized.trim().split(/\r?\n/);
    if (!rawLines || rawLines.length === 0) return { headers: [], data: [], delimiter: ',' };

    // 简单检测分隔符：如果头行中制表符数量 >= 逗号数量且存在制表符，则视为 TSV
    const firstLine = rawLines[0];
    const commaCount = (firstLine.match(/,/g) || []).length;
    const tabCount = (firstLine.match(/\t/g) || []).length;
    const delimiter = tabCount >= commaCount && tabCount > 0 ? '\t' : ',';

    // 记录最近一次检测到的分隔符
    lastDetectedDelimiter = delimiter;
    // 调试信息（在浏览器控制台可见）
    try {
        console.debug('[parser] detected delimiter:', JSON.stringify(delimiter));
        console.debug('[parser] raw header line:', rawLines[0]);
    } catch (e) {}

    let headers = parseCSVLine(rawLines[0], delimiter);
    // 容错：如果头部解析成单一字段但包含分隔符，则先展开为多个头部（这样后续 data 对象的键会与头部一致）
    if (headers.length === 1 && headers[0] && headers[0].includes(delimiter)) {
        headers = headers[0].split(delimiter).map(h => h.trim());
    }
    const data = [];
    for (let i = 1; i < rawLines.length; i++) {
        if (rawLines[i].trim() === '') continue;
        let values = parseCSVLine(rawLines[i], delimiter);
        // 容错：如果解析结果只有一个字段但包含分隔符，尝试简单分割（处理某些粘贴/编码异常）
        if (values.length === 1 && values[0].includes(delimiter)) {
            values = values[0].split(delimiter).map(v => v.trim());
        }
        const obj = {};
        for (let j = 0; j < headers.length; j++) {
            obj[headers[j]] = values[j] || '';
        }
        data.push(obj);
    }

    return { headers, data, delimiter };
}

/**
 * 解析 CSV 行
 */
function parseCSVLine(line, delimiter = ',') {
    const result = [];
    let current = '';
    let insideQuotes = false;

    for (let i = 0; i < line.length; i++) {
        const char = line[i];
        const nextChar = line[i + 1];

        if (char === '"') {
            if (insideQuotes && nextChar === '"') {
                current += '"';
                i++;
            } else {
                insideQuotes = !insideQuotes;
            }
        } else if (char === delimiter && !insideQuotes) {
            result.push(current.trim());
            current = '';
        } else {
            current += char;
        }
    }

    result.push(current.trim());
    return result;
}

/**
 * JSON 数组转 CSV
 */
function arrayToCSV(headers, data, delimiter = ',') {
    const lines = [];

    // 添加头部
    lines.push(headers.map(h => escapeCSV(h, delimiter)).join(delimiter === '\t' ? '\t' : ','));

    // 添加数据
    for (const row of data) {
        const values = headers.map(h => escapeCSV(String(row[h] || ''), delimiter));
        lines.push(values.join(delimiter === '\t' ? '\t' : ','));
    }

    return lines.join('\n');
}

/**
 * 转义 CSV 值
 */
function escapeCSV(value, delimiter = ',') {
    // 默认按逗号分隔规则处理；如果是 TSV，也按类似规则处理（只在必要时加引号）
    return escapeCSVWithDelimiter(value, delimiter);
}

function escapeCSVWithDelimiter(value, delimiter) {
    const needsQuote = value.includes('"') || value.includes('\n') || (delimiter === ',' ? value.includes(',') : value.includes('\t'));
    if (needsQuote) {
        return '"' + value.replace(/"/g, '""') + '"';
    }
    return value;

/**
 * 尝试解析 JSON
 */

}

/**
 * 尝试解析 JSON
 */
// 不再支持 JSON 输入：前端只处理 CSV/TSV 文本
// 不再支持 JSON 输入：前端只处理 CSV/TSV 文本

// ==================== 转换逻辑 ====================

/**
 * 宽格式转长格式
 */
function wideToLong(data, idVars, valueVars = null, varName = 'variable', valueName = 'value') {
    // 标准化 idVars
    const idVarsArray = typeof idVars === 'string' 
        ? idVars.split(',').map(v => v.trim()) 
        : idVars;

    // 确定要转换的列
    const allColumns = Object.keys(data[0] || {});
    let valueVarsArray = valueVars;
    
    if (!valueVars) {
        valueVarsArray = allColumns.filter(col => !idVarsArray.includes(col));
    } else {
        valueVarsArray = typeof valueVars === 'string' 
            ? valueVars.split(',').map(v => v.trim()) 
            : valueVars;
    }

    const result = [];

    for (const row of data) {
        for (const varCol of valueVarsArray) {
            const newRow = {};
            
            // 复制 ID 列
            for (const idCol of idVarsArray) {
                newRow[idCol] = row[idCol];
            }
            
            // 添加变量和值
            newRow[varName] = varCol;
            newRow[valueName] = row[varCol];
            
            result.push(newRow);
        }
    }

    return result;
}

/**
 * 长格式转宽格式
 */
function longToWide(data, indexCols, columnCol, valueCol) {
    // 标准化参数
    const indexColsArray = typeof indexCols === 'string' 
        ? indexCols.split(',').map(v => v.trim()) 
        : indexCols;

    const result = {};
    const columnValues = new Set();

    // 第一次遍历：收集所有列值
    for (const row of data) {
        const colValue = String(row[columnCol]);
        columnValues.add(colValue);
    }

    // 第二次遍历：构建宽格式
    for (const row of data) {
        // 创建索引键
        const indexKey = indexColsArray.map(col => String(row[col])).join('|||');
        
        if (!result[indexKey]) {
            result[indexKey] = {};
            
            // 初始化索引列
            for (const col of indexColsArray) {
                result[indexKey][col] = row[col];
            }
            
            // 初始化值列
            for (const colValue of columnValues) {
                result[indexKey][colValue] = '';
            }
        }
        
        // 填充值
        const colValue = String(row[columnCol]);
        result[indexKey][colValue] = row[valueCol];
    }

    // 转换回数组
    return Object.values(result);
}

/**
 * 自动检测数据格式
 */
function detectFormat(data) {
    if (!data || data.length === 0) return null;
    
    const firstRow = data[0];
    const columns = Object.keys(firstRow);
    
    // 简单启发式：如果有 'variable' 或 'value' 列，可能是长格式
    const hasVarOrValue = columns.some(col => 
        col.toLowerCase().includes('variable') || 
        col.toLowerCase().includes('value') ||
        col.toLowerCase().includes('metric')
    );
    
    return hasVarOrValue ? 'long' : 'wide';
}

// ==================== UI 交互 ====================

/**
 * 切换输入模式
 */
function switchInputMode(mode) {
    const textInput = document.getElementById('textInput');
    const fileInput = document.getElementById('fileInput');
    const buttons = document.querySelectorAll('.toggle-btn');
    
    buttons.forEach((btn, idx) => {
        if ((idx === 0 && mode === 'text') || (idx === 1 && mode === 'file')) {
            btn.classList.add('active');
        } else {
            btn.classList.remove('active');
        }
    });
    
    if (mode === 'text') {
        textInput.style.display = 'block';
        fileInput.style.display = 'none';
    } else {
        textInput.style.display = 'none';
        fileInput.style.display = 'block';
    }
}

/**
 * 处理文件上传
 */
function handleFileUpload(event) {
    const file = event.target.files[0];
    if (!file) return;

    // 校验扩展名，仅允许 .csv 或 .tsv
    const name = file.name || '';
    const lower = name.toLowerCase();
    if (!(lower.endsWith('.csv') || lower.endsWith('.tsv'))) {
        showError('仅支持 CSV (.csv) 或 TSV (.tsv) 文件');
        event.target.value = '';
        return;
    }

    const reader = new FileReader();
    reader.onload = function(e) {
        const content = e.target.result;
        document.getElementById('dataInput').value = content;
    };
    reader.readAsText(file);
}

/**
 * 转换模式改变
 */
document.addEventListener('DOMContentLoaded', function() {
    const modeSelect = document.getElementById('conversionMode');
    if (modeSelect) {
        modeSelect.addEventListener('change', function() {
            const wide2longOptions = document.getElementById('wide2longOptions');
            const long2wideOptions = document.getElementById('long2wideOptions');
            
            if (this.value === 'wide2long') {
                wide2longOptions.style.display = 'block';
                long2wideOptions.style.display = 'none';
            } else {
                wide2longOptions.style.display = 'none';
                long2wideOptions.style.display = 'block';
            }
        });
    }
});

/**
 * 转换数据
 */
function convertData() {
    try {
        const input = document.getElementById('dataInput').value.trim();
        if (!input) {
            showError('请输入数据');
            return;
        }
        // 仅解析 CSV/TSV 文本（支持逗号或制表符分隔）
        const parsed = csvToArray(input);
        if (!parsed || !parsed.data || parsed.data.length === 0) {
            showError('无法解析数据，请确保为 CSV 或 TSV 文本');
            return;
        }

        const data = parsed.data;
        const headers = parsed.headers || Object.keys(data[0]);
        const mode = document.getElementById('conversionMode').value;

        let resultData;

        if (mode === 'wide2long') {
            const idVars = document.getElementById('idVars').value;
            if (!idVars) {
                showError('请输入 ID 列');
                return;
            }

            const varName = document.getElementById('varName').value || 'variable';
            const valueName = document.getElementById('valueName').value || 'value';

            resultData = wideToLong(data, idVars, null, varName, valueName);
        } else {
            const indexCols = document.getElementById('indexCol').value;
            const columnCol = document.getElementById('columnCol').value;
            const valueCol = document.getElementById('valueCol').value;

            if (!indexCols || !columnCol || !valueCol) {
                showError('请填写所有必需的列参数');
                return;
            }

            resultData = longToWide(data, indexCols, columnCol, valueCol);
        }

    // 生成输出
    const resultHeaders = Object.keys(resultData[0] || {});
    const outDelimiter = (parsed && parsed.delimiter) ? parsed.delimiter : lastDetectedDelimiter;
    const resultCSV = arrayToCSV(resultHeaders, resultData, outDelimiter);

        document.getElementById('dataOutput').value = resultCSV;
        showSuccess('转换成功！');
    } catch (error) {
        showError('转换失败: ' + error.message);
        console.error(error);
    }
}

/**
 * 复制输出
 */
function copyOutput() {
    const output = document.getElementById('dataOutput');
    if (!output.value) {
        showError('没有可复制的数据');
        return;
    }

    output.select();
    document.execCommand('copy');
    showSuccess('已复制到剪贴板！');
}

/**
 * 下载输出
 */
function downloadOutput() {
    const output = document.getElementById('dataOutput').value;
    if (!output) {
        showError('没有可下载的数据');
        return;
    }

    // 根据最后检测到的分隔符选择后缀和 MIME
    const isTSV = lastDetectedDelimiter === '\t';
    const mime = isTSV ? 'text/tab-separated-values;charset=utf-8;' : 'text/csv;charset=utf-8;';
    const ext = isTSV ? 'tsv' : 'csv';

    const blob = new Blob([output], { type: mime });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = `data_${new Date().getTime()}.${ext}`;
    link.click();
    showSuccess('文件已下载！');
}

/**
 * 清空输入
 */
function clearInput() {
    document.getElementById('dataInput').value = '';
    document.getElementById('idVars').value = '';
    document.getElementById('indexCol').value = '';
    document.getElementById('columnCol').value = '';
    document.getElementById('valueCol').value = '';
}

/**
 * 清空输出
 */
function clearOutput() {
    document.getElementById('dataOutput').value = '';
}

/**
 * 显示成功消息
 */
function showSuccess(msg) {
    const element = document.getElementById('successMessage');
    element.textContent = '✓ ' + msg;
    element.style.display = 'block';
    setTimeout(() => {
        element.style.display = 'none';
    }, 3000);
}

/**
 * 显示错误消息
 */
function showError(msg) {
    const element = document.getElementById('errorMessage');
    element.textContent = '✗ ' + msg;
    element.style.display = 'block';
    setTimeout(() => {
        element.style.display = 'none';
    }, 3000);
}

/**
 * 显示示例
 */
function showExample(index) {
    const tabs = document.querySelectorAll('.example-tab');
    const contents = document.querySelectorAll('.example-content');

    tabs.forEach((tab, i) => {
        if (i === index) {
            tab.classList.add('active');
            contents[i].classList.add('active');
        } else {
            tab.classList.remove('active');
            contents[i].classList.remove('active');
        }
    });
}

/**
 * 显示关于信息
 */
function showAbout() {
    alert('数据格式转换工具 v1.0\n\n' +
          '这是一个在线数据转换工具，支持：\n' +
          '• 宽格式转长格式\n' +
          '• 长格式转宽格式\n' +
          '• CSV / TSV 文本导入/导出\n\n' +
          'Made with ❤️ for data analysis\n' +
          'MIT License');
}

// 页面加载完成后的初始化
document.addEventListener('DOMContentLoaded', function() {
    // 默认示例数据
    const defaultExample = `id,name,Math,English,Science
1,Alice,85,92,88
2,Bob,90,88,92`;
    
    document.getElementById('dataInput').placeholder = '将数据粘贴到这里...\n\n例如:\n' + defaultExample;
});
