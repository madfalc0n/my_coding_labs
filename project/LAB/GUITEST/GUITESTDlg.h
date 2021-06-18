
// GUITESTDlg.h: 헤더 파일
//

#pragma once


// CGUITESTDlg 대화 상자
class CGUITESTDlg : public CDialogEx
{
// 생성입니다.
private:
	CImage m_image;
	CImage m_image1;
	

public:
	CGUITESTDlg(CWnd* pParent = nullptr);	// 표준 생성자입니다.
	void show(int h, int w);
	void scaleup(int h, int w);

// 대화 상자 데이터입니다.
#ifdef AFX_DESIGN_TIME
	enum { IDD = IDD_GUITEST_DIALOG };
#endif

	protected:
	virtual void DoDataExchange(CDataExchange* pDX);	// DDX/DDV 지원입니다.


// 구현입니다.
protected:
	HICON m_hIcon;

	// 생성된 메시지 맵 함수
	virtual BOOL OnInitDialog();
	afx_msg void OnSysCommand(UINT nID, LPARAM lParam);
	afx_msg void OnPaint();
	afx_msg HCURSOR OnQueryDragIcon();
	DECLARE_MESSAGE_MAP()
public:
	afx_msg void OnBnClickedButton1();
	CString edit_result;
	afx_msg void OnEnChangeEdit1();
};
