import React, { Suspense, lazy, useState, useEffect, useRef, useCallback } from 'react';
import { Play } from 'lucide-react';
import styles from './CodeRunner.module.css';

const MonacoEditor = lazy(() => import('@monaco-editor/react'));

const CodeRunner = ({ initialCode = "# 在这里写下你的 Python 代码\nprint('Hello, World!')" }) => {
  const [code, setCode] = useState(initialCode);
  const [output, setOutput] = useState('');
  const [isRunning, setIsRunning] = useState(false);
  const [pyodide, setPyodide] = useState(null);
  const [isPyodideLoading, setIsPyodideLoading] = useState(true);
  const [isActivated, setIsActivated] = useState(false);
  const [editorWidth, setEditorWidth] = useState(50);
  const [isResizing, setIsResizing] = useState(false);
  const containerRef = useRef(null);

  useEffect(() => {
    setCode(initialCode);
  }, [initialCode]);

  useEffect(() => {
    if (!isActivated) return undefined;

    let script;
    const initPyodide = async () => {
      try {
        setIsPyodideLoading(true);

        if (!window.loadPyodide) {
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

    return () => {};
  }, [isActivated]);

  const handleMouseDown = useCallback((e) => {
    e.preventDefault();
    setIsResizing(true);
  }, []);

  const handleMouseMove = useCallback((e) => {
    if (!isResizing || !containerRef.current) return;
    
    const containerRect = containerRef.current.getBoundingClientRect();
    const newWidth = ((e.clientX - containerRect.left) / containerRect.width) * 100;
    setEditorWidth(Math.min(Math.max(newWidth, 20), 80));
  }, [isResizing]);

  const handleMouseUp = useCallback(() => {
    setIsResizing(false);
  }, []);

  useEffect(() => {
    if (isResizing) {
      document.addEventListener('mousemove', handleMouseMove);
      document.addEventListener('mouseup', handleMouseUp);
      document.body.style.cursor = 'col-resize';
      document.body.style.userSelect = 'none';
    }
    
    return () => {
      document.removeEventListener('mousemove', handleMouseMove);
      document.removeEventListener('mouseup', handleMouseUp);
      document.body.style.cursor = '';
      document.body.style.userSelect = '';
    };
  }, [isResizing, handleMouseMove, handleMouseUp]);

  const isValidPythonCode = (code) => {
    const trimmed = code.trim();
    if (!trimmed) return false;
    const invalidPatterns = [
        /^(输入|请|使用|定义|计算|判断|创建|打印)/,
        /^# .*$/,
    ];
    for (const pattern of invalidPatterns) {
        if (pattern.test(trimmed) && !trimmed.includes('\n')) return false;
    }
    return true;
  };

  const handleRun = async () => {
    if (!pyodide || !code.trim()) return;
    
    if (!isValidPythonCode(code)) {
        setOutput('[错误] 请输入有效的 Python 代码！\n提示：不能只是纯文本描述，需要是真正的 Python 代码。');
        return;
    }

    setIsRunning(true);
    setOutput('正在运行...');
    
    try {
        pyodide.setStdout({
            batched: (msg) => {
                setOutput(prev => (prev === '正在运行...' ? msg : prev + '\n' + msg));
            }
        });

        pyodide.setStderr({
            batched: (msg) => {
                setOutput(prev => (prev === '正在运行...' ? msg : prev + '\n' + msg));
            }
        });

        let inputBuffer = [];
        let inputIndex = 0;
        
        pyodide.setStdin({
            stdin: () => {
                if (inputIndex < inputBuffer.length) {
                    return inputBuffer[inputIndex++] + '\n';
                }
                const result = window.prompt("请输入内容 (直接确定即可):");
                return (result || '') + '\n';
            }
        });

        await pyodide.runPythonAsync(code);
    } catch (error) {
         const errorMsg = String(error);
         if (errorMsg.includes("EOFError") || errorMsg.includes("I/O error")) {
             setOutput(prev => prev + '\n[提示] 代码执行完成（或需要输入）');
         } else {
             setOutput(errorMsg);
         }
    } finally {
        setIsRunning(false);
    }
  };

  const editorPaneWidth = `${editorWidth}%`;
  const outputPaneWidth = `${100 - editorWidth}%`;

  if (!isActivated) {
    return (
      <div className={styles.container}>
        <div className={styles.header}>
          <span className={styles.fileName}>practice.py</span>
          <button
            onClick={() => setIsActivated(true)}
            className={styles.runButton}
            type="button"
          >
            打开练习区
          </button>
        </div>
        <div className={styles.output}>
          <div className={styles.outputLabel}>延迟加载</div>
          <pre className={styles.outputPre}>
            练习区会在你真正需要时再加载编辑器和 Python 运行环境，这样课程页面会更快打开。
          </pre>
        </div>
      </div>
    );
  }

  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <span className={styles.fileName}>main.py</span>
        <button 
          onClick={handleRun}
          disabled={isRunning || isPyodideLoading}
          className={styles.runButton}
        >
          <Play size={14} />
          {isPyodideLoading ? '加载环境...' : isRunning ? '运行中...' : '运行代码'}
        </button>
      </div>
      <div className={styles.editorWrapper} ref={containerRef}>
        <div className={styles.editorPane} style={{ width: editorPaneWidth }}>
          <Suspense fallback={<div className={styles.output}>编辑器加载中...</div>}>
            <MonacoEditor
              height="100%"
              defaultLanguage="python"
              value={code}
              onChange={(value) => setCode(value || '')}
              theme="vs-dark"
              options={{
                minimap: { enabled: false },
                fontSize: 14,
                scrollBeyondLastLine: false,
                automaticLayout: true,
                lineNumbers: 'on',
                glyphMargin: false,
                lineDecorationsWidth: 0,
                lineNumbersMinChars: 5,
                renderLineHighlight: 'none',
                overviewRulerBorder: false,
                hideCursorInOverviewRuler: true,
                padding: { top: 8, bottom: 8 },
                readOnly: false,
                wordWrap: 'on',
                scrollbar: {
                  vertical: 'auto',
                  horizontal: 'auto',
                  verticalScrollbarSize: 10,
                  horizontalScrollbarSize: 10,
                },
              }}
            />
          </Suspense>
        </div>
        <div 
          className={styles.resizer}
          onMouseDown={handleMouseDown}
        />
        <div className={styles.editorPane} style={{ width: outputPaneWidth }}>
            <div className={styles.output}>
              <div className={styles.outputLabel}>终端输出</div>
              <pre className={styles.outputPre}>{output}</pre>
            </div>
        </div>
      </div>
    </div>
  );
};

export default CodeRunner;
