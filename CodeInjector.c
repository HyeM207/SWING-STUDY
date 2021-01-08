#include <stdio.h>
#include <Windows.h>

typedef UINT(WINAPI* WINEXEC)(LPCSTR, UINT);  //함수 포인터


//Thread Parameter
typedef struct _THREAD_PARAM
{
    FARPROC pFunc[2];  //LoadLibraryA(), GetProcAddress()
    char szBuf[4][128];  //"user32.dll", "MessageBoxA", "www.reversecore.com", "ReverseCore"

} THREAD_PARAM, * PTHREAD_PARAM;


// LoadLibraryA()
typedef HMODULE(WINAPI* PFLOADLIBRARYA)
(
    LPCSTR lpLibFileName
    );

// GetProcAddress()
typedef FARPROC(WINAPI* PFGETPROCADDRESS)
(
    HMODULE hModule,
    LPCSTR lpProcName
    );

// MessageBoxA()
typedef int (WINAPI* PFMESSAGEBOXA)
(
    HWND hWnd,
    LPCSTR lpText,
    LPCSTR lpCaption,
    UINT uType
    );


DWORD WINAPI ThreadProc(LPVOID lParam)
{
    PTHREAD_PARAM pParam = (PTHREAD_PARAM)lParam;
    HMODULE hMod = NULL;
    FARPROC pFunc = NULL;

    // hMod= LoadLibraryA("user32.dll");
    hMod = ((PFLOADLIBRARYA)pParam->pFunc[0])(pParam->szBuf[0]);

    // pFunc = GetProcAddress(hMod, "MesageBoxA");
    pFunc = (FARPROC)((PFGETPROCADDRESS)pParam->pFunc[1])(hMod, pParam->szBuf[1]);

    // pFunc(NULL, "www.reversecore.com", "ReverseCore", MB_OK);
    ((PFMESSAGEBOXA)pFunc)(NULL, pParam->szBuf[2], pParam->szBuf[3], MB_OK);

    return 0;
}


// CodeInjection 핵심 함수
BOOL InjectCode(DWORD dwPID)
{
    HMODULE hMod = NULL;
    THREAD_PARAM param = { 0, };  
    HANDLE hProcess = NULL;
    HANDLE hThread = NULL;
    LPVOID pRemoteBuf[2] = { 0, };
    DWORD dwSize = 0;


    // 0. 모듈에 대한 핸들 검색
    hMod = GetModuleHandleA("kernel32.dll");

    // 1.  THREAD_PARAM 설정
    param.pFunc[0] = GetProcAddress(hMod, "LoadLibraryA");
    param.pFunc[1] = GetProcAddress(hMod, "GetProcAddress");
    strcpy(param.szBuf[0], "user32.dll");
    strcpy(param.szBuf[1], "MessageBoxA");
    strcpy(param.szBuf[2], "www.reversecore.com");
    strcpy(param.szBuf[3], "ReverseCore");

    // 2. 프로세스 열기 
    hProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, dwPID);


    // 3. THREAD_PARAM 공간 확보
    dwSize = sizeof(THREAD_PARAM);
    pRemoteBuf[0] = VirtualAllocEx(hProcess, NULL, dwSize, MEM_COMMIT, PAGE_READWRITE);
    
    //WriteProcessMemory(hProcess, lpBaseAddress , lpBuffer,  nSize , [out],  lpNumberOfBytesWritten)
    WriteProcessMemory(hProcess, pRemoteBuf[0], (LPVOID)&param, dwSize, NULL); 


     // 4. ThreadProc() 공간 확보
    dwSize = (DWORD)InjectCode - (DWORD)ThreadProc;
    

    // 4-01. 공간 확보
    //VirtualAllocEx(hProcess, lpAddress, dwSize, flAllocationType, flProtect);
    pRemoteBuf[1] = VirtualAllocEx(hProcess, NULL, dwSize, MEM_COMMIT, PAGE_EXECUTE_READWRITE);
    
    // 4-02. 메모리에 쓰기
    //WriteProcessMemory(hProcess, lpBaseAddress, lpBuffer, nSize, [out], lpNumberOfBytesWritten);
    WriteProcessMemory(hProcess, pRemoteBuf[1], (LPVOID)ThreadProc, dwSize, NULL);
  
    // 4-03. 쓰레드 생성
    //CreateRemoteThread(hProcess, lpThreadAttributes, dwStackSize, lpParameter, dwCreationFlags, lpThreadId);
    hThread = CreateRemoteThread(hProcess, NULL, 0, (LPTHREAD_START_ROUTINE)pRemoteBuf[1], pRemoteBuf[0], 0, NULL);
   
    // 커널 오브젝트의 상태정보를 확인
    WaitForSingleObject(hThread, INFINITE);
    
    
    CloseHandle(hThread);
    CloseHandle(hProcess);

    return TRUE;
}



int main(int argc, char* argv[])
{
    int getPID = 0;

    printf("PID :");
    scanf("%d", &getPID);

    // Code Injection
    InjectCode(getPID);

    return 0;
}
