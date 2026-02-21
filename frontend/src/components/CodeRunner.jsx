import React, { useState, useEffect } from 'react';
import { Play } from 'lucide-react';
import Editor from "@monaco-editor/react";

const CodeRunner = ({ initialCode = "# 在这里写下你的 Python 代码\nprint('Hello, World!')" }) => {
  const [code, setCode] = useState(initialCode);
  const [output, setOutput] = useState('');
  const [isRunning, setIsRunning] = useState(false);
  const [pyodide, setPyodide] = useState(null);
  const [isPyodideLoading, setIsPyodideLoading] = useState(true);

  useEffect(() => {
    setCode(initialCode);
  }, [initialCode]);

  useEffect(() => {
    let script;
    const initPyodide = async () => {
      try {
        if (!window.loadPyodide) {
            // 如果已经在加载中，等待之前的加载完成
            if (window.pyodideLoadingPromise) {
                await window.pyodideLoadingPromise;
            } else {
                script = document.createElement('script');
                script.src = "https://cdn.jsdelivr.net/pyodide/v0.25.0/full/pyodide.js";
                script.async = true;
                document.body.appendChild(script);
                
                window.pyodideLoadingPromise = new Promise((resolve, reject) => {
                    script.onload = resolve;
                    script.onerror = reject;
                });
                await window.pyodideLoadingPromise;
            }
        }

        if (window.loadPyodide) {
             // 确保不重复加载
             if (!window.pyodideInstance) {
                 window.pyodideInstance = await window.loadPyodide({
                     indexURL: "https://cdn.jsdelivr.net/pyodide/v0.25.0/full/"
                 });
             }
             setPyodide(window.pyodideInstance);
        }
        setIsPyodideLoading(false);
      } catch (error) {
        console.error("Pyodide loading failed:", error);
        setOutput(`Python 环境加载失败: ${error.message}\n请检查网络连接并刷新页面重试。`);
        setIsPyodideLoading(false);
      }
    };
    initPyodide();

    return () => {
        // Cleanup if needed
    };
  }, []);

  const handleRun = async () => {
    if (!pyodide) return;

    setIsRunning(true);
    setOutput('正在运行...');
    
    try {
        // 重定向 stdout
        pyodide.setStdout({
            batched: (msg) => {
                setOutput(prev => (prev === '正在运行...' ? msg : prev + '\n' + msg));
            }
        });

        // 关键修复：Pyodide 的 stdin 配置需要正确返回字符
        // 在新版本 Pyodide 中，setStdin 接受一个选项对象 { stdin: ... }
        // 确保不要混用其他参数
        
        pyodide.setStdin({
            stdin: () => {
                const result = window.prompt("请输入内容:");
                // 如果用户点击取消，返回空字符串
                if (result === null) return ""; 
                return result;
            }
        });

        // 确保使用 runPythonAsync
        await pyodide.runPythonAsync(code);
    } catch (error) {
         // 捕获特定 IO 错误并给出更友好的提示
         if (String(error).includes("OSError: [Errno 29] I/O error")) {
             setOutput(prev => prev + '\n[系统提示] 无法读取输入。请尝试刷新页面重试，或检查浏览器是否拦截了弹窗。');
         } else {
             setOutput(String(error));
         }
    } finally {
        setIsRunning(false);
    }
  };

  return (
    <div className="bg-slate-900 rounded-lg overflow-hidden border border-slate-700 font-mono text-sm">
      <div className="flex items-center justify-between bg-slate-800 p-2 border-b border-slate-700">
        <span className="text-slate-400 px-2">main.py</span>
        <button 
          onClick={handleRun}
          disabled={isRunning || isPyodideLoading}
          className="flex items-center gap-2 bg-green-600 hover:bg-green-700 text-white px-3 py-1 rounded transition-colors disabled:opacity-50"
        >
          <Play size={14} />
          {isPyodideLoading ? '加载环境...' : isRunning ? '运行中...' : '运行代码'}
        </button>
      </div>
      <div className="grid grid-cols-1 md:grid-cols-2 h-64">
        <div className="w-full h-full">
            <Editor
                height="100%"
                defaultLanguage="python"
                value={code}
                onChange={(value) => setCode(value)}
                theme="vs-dark"
                options={{
                    minimap: { enabled: false },
                    fontSize: 14,
                    scrollBeyondLastLine: false,
                    automaticLayout: true,
                }}
            />
        </div>
        <div className="bg-black text-green-400 p-4 border-t md:border-t-0 md:border-l border-slate-700 font-mono overflow-auto">
          <div className="uppercase text-xs text-slate-500 mb-2">终端输出</div>
          <pre className="whitespace-pre-wrap">{output}</pre>
        </div>
      </div>
    </div>
  );
};

export default CodeRunner;
