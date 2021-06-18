
// GUITESTDlg.cpp: 구현 파일
//

#include "pch.h"
#include "framework.h"
#include "GUITEST.h"
#include "GUITESTDlg.h"
#include "afxdialogex.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif


// 응용 프로그램 정보에 사용되는 CAboutDlg 대화 상자입니다.

class CAboutDlg : public CDialogEx
{
public:
	CAboutDlg();

// 대화 상자 데이터입니다.
#ifdef AFX_DESIGN_TIME
	enum { IDD = IDD_ABOUTBOX };
#endif

	protected:
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV 지원입니다.

// 구현입니다.
protected:
	DECLARE_MESSAGE_MAP()
};

CAboutDlg::CAboutDlg() : CDialogEx(IDD_ABOUTBOX)
{
}

void CAboutDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialogEx::DoDataExchange(pDX);
}

BEGIN_MESSAGE_MAP(CAboutDlg, CDialogEx)
END_MESSAGE_MAP()


// CGUITESTDlg 대화 상자



CGUITESTDlg::CGUITESTDlg(CWnd* pParent /*=nullptr*/)
	: CDialogEx(IDD_GUITEST_DIALOG, pParent)
	, edit_result(_T(""))
{
	m_hIcon = AfxGetApp()->LoadIcon(IDR_MAINFRAME);
}

void CGUITESTDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialogEx::DoDataExchange(pDX);
	
}

BEGIN_MESSAGE_MAP(CGUITESTDlg, CDialogEx)
	ON_WM_SYSCOMMAND()
	ON_WM_PAINT()
	ON_WM_QUERYDRAGICON()
	ON_BN_CLICKED(IDC_BUTTON1, &CGUITESTDlg::OnBnClickedButton1)
END_MESSAGE_MAP()


// CGUITESTDlg 메시지 처리기

BOOL CGUITESTDlg::OnInitDialog()
{
	CDialogEx::OnInitDialog();

	// 시스템 메뉴에 "정보..." 메뉴 항목을 추가합니다.

	// IDM_ABOUTBOX는 시스템 명령 범위에 있어야 합니다.
	ASSERT((IDM_ABOUTBOX & 0xFFF0) == IDM_ABOUTBOX);
	ASSERT(IDM_ABOUTBOX < 0xF000);

	CMenu* pSysMenu = GetSystemMenu(FALSE);
	if (pSysMenu != nullptr)
	{
		BOOL bNameValid;
		CString strAboutMenu;
		bNameValid = strAboutMenu.LoadString(IDS_ABOUTBOX);
		ASSERT(bNameValid);
		if (!strAboutMenu.IsEmpty())
		{
			pSysMenu->AppendMenu(MF_SEPARATOR);
			pSysMenu->AppendMenu(MF_STRING, IDM_ABOUTBOX, strAboutMenu);
		}
	}

	// 이 대화 상자의 아이콘을 설정합니다.  응용 프로그램의 주 창이 대화 상자가 아닐 경우에는
	//  프레임워크가 이 작업을 자동으로 수행합니다.
	SetIcon(m_hIcon, TRUE);			// 큰 아이콘을 설정합니다.
	SetIcon(m_hIcon, FALSE);		// 작은 아이콘을 설정합니다.

	// TODO: 여기에 추가 초기화 작업을 추가합니다.
	m_image.Load(L"Lenna.png");


	return TRUE;  // 포커스를 컨트롤에 설정하지 않으면 TRUE를 반환합니다.
}

void CGUITESTDlg::OnSysCommand(UINT nID, LPARAM lParam)
{
	if ((nID & 0xFFF0) == IDM_ABOUTBOX)
	{
		CAboutDlg dlgAbout;
		dlgAbout.DoModal();
	}
	else
	{
		CDialogEx::OnSysCommand(nID, lParam);
	}
}

// 대화 상자에 최소화 단추를 추가할 경우 아이콘을 그리려면
//  아래 코드가 필요합니다.  문서/뷰 모델을 사용하는 MFC 애플리케이션의 경우에는
//  프레임워크에서 이 작업을 자동으로 수행합니다.

void CGUITESTDlg::OnPaint()
{
	if (IsIconic())
	{
		CPaintDC dc(this); // 그리기를 위한 디바이스 컨텍스트입니다.

		SendMessage(WM_ICONERASEBKGND, reinterpret_cast<WPARAM>(dc.GetSafeHdc()), 0);

		// 클라이언트 사각형에서 아이콘을 가운데에 맞춥니다.
		int cxIcon = GetSystemMetrics(SM_CXICON);
		int cyIcon = GetSystemMetrics(SM_CYICON);
		CRect rect;
		GetClientRect(&rect);
		int x = (rect.Width() - cxIcon + 1) / 2;
		int y = (rect.Height() - cyIcon + 1) / 2;

		// 아이콘을 그립니다.
		dc.DrawIcon(x, y, m_hIcon);
	}
	else
	{
		CDialogEx::OnPaint();
	}
}

// 사용자가 최소화된 창을 끄는 동안에 커서가 표시되도록 시스템에서
//  이 함수를 호출합니다.
HCURSOR CGUITESTDlg::OnQueryDragIcon()
{
	return static_cast<HCURSOR>(m_hIcon);
}

void CGUITESTDlg::show(int width, int height)
{
	int arr[1][1][3] = { 200, };
	for (int y = 0; y < height; y++) {
		for (int x = 0; x < width; x++) {
			/*BYTE R = GetRValue(origin_image.GetPixel(x, y));
			BYTE G = GetGValue(origin_image.GetPixel(x, y));
			BYTE B = GetBValue(origin_image.GetPixel(x, y));*/
			//if (x > rand()%400 && x < 400 && y > 200 && y < 400)
			//{
			//	m_image.SetPixel(x, y, RGB(0, 0, 0)); // m_image1에 픽셀값을 그린다.
			//}
			//else {
			//	m_image.SetPixel(x, y, RGB(255, 255, 255)); // m_image1에 픽셀값을 그린다.
			//}
			m_image.SetPixel(x, y, RGB(arr[0][0][0], arr[0][0][1], arr[0][0][2])); // m_image1에 픽셀값을 그린다.
		}
	}
}

void CGUITESTDlg::scaleup(int width, int height)
{	
	int h = m_image.GetHeight(); // 높이 저장하는 변수
	int w = m_image.GetWidth(); // 넓이 저장하는 변수
	int rate_2 = 2; // 2배
	m_image1.Create(m_image.GetWidth() * 2, m_image.GetHeight() * 2, m_image.GetBPP(), 0);
	for (int y = 0; y < rate_2 * h; y++) {
		for (int x = 0; x < rate_2 * w; x++) {
			BYTE R = GetRValue(m_image.GetPixel(x / rate_2, y / rate_2));
			BYTE G = GetGValue(m_image.GetPixel(x / rate_2, y / rate_2));
			BYTE B = GetBValue(m_image.GetPixel(x / rate_2, y / rate_2));
			m_image1.SetPixel(x, y, RGB(R, G, B)); // m_image1에 픽셀값을 그린다.
		}
	}
}


void CGUITESTDlg::OnBnClickedButton1()
{
	// TODO: 여기에 컨트롤 알림 처리기 코드를 추가합니다.
	CClientDC dc(this);

	clock_t startTime, endTime;
	startTime = clock();
	show(256,256);
	//scaleup(256, 256);
	m_image.Draw(dc, 10, 10);
	endTime = clock();
	printf("수행 시간 : %f\n", ((double)(endTime - startTime)) / CLOCKS_PER_SEC);

}
