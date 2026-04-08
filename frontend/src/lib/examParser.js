export function parseExamMarkdown(markdown) {
  const text = markdown || '';
  const lines = text.split('\n');
  const titleLine = lines.find((line) => line.startsWith('# '));
  const title = titleLine ? titleLine.replace('# ', '').trim() : '未命名试卷';

  const durationMatch = text.match(/考试时间：\s*([0-9]+)\s*分钟/);
  const totalScoreMatch = text.match(/满分：\s*([0-9]+)\s*分/);

  const questionBlocks = text.split(/^###\s+/m).slice(1);
  const questions = questionBlocks.map((block) => {
    const cleaned = block.trim();
    const firstLineEnd = cleaned.indexOf('\n');
    const number = firstLineEnd > -1 ? cleaned.slice(0, firstLineEnd).trim() : cleaned;
    const body = firstLineEnd > -1 ? cleaned.slice(firstLineEnd + 1) : '';

    const questionMatch = body.match(/题目：\s*(.+)/);
    const answerMatch = body.match(/答案：\s*([A-D])/i);
    const explanationMatch = body.match(/解析：\s*(.+)/);

    const options = ['A', 'B', 'C', 'D']
      .map((key) => {
        const match = body.match(new RegExp(`^${key}\\.\\s*(.+)$`, 'm'));
        return match ? { key, text: match[1].trim() } : null;
      })
      .filter(Boolean);

    return {
      number,
      question: questionMatch ? questionMatch[1].trim() : '',
      options,
      answer: answerMatch ? answerMatch[1].toUpperCase() : null,
      explanation: explanationMatch ? explanationMatch[1].trim() : '',
    };
  });

  return {
    title,
    duration_minutes: durationMatch ? Number(durationMatch[1]) : 60,
    total_score: totalScoreMatch ? Number(totalScoreMatch[1]) : 100,
    questions,
  };
}
