from django.core.paginator import Paginator

def pagination(request, Board, contents_num = 5) -> dict:
    all_boards = Board.objects.order_by('-id')
    board_page = int(request.GET.get('page',1))
    paginator = Paginator(all_boards, contents_num)
    boards = paginator.get_page(board_page)
    now_page = boards.number
    end_page = boards.paginator.num_pages

    if end_page >= 7:
        min_page = 7
    else:
        min_page = end_page

    display_page = {}
    if min_page < 7:
        for k in range(min_page):
            display_page[k] = k+1
    elif now_page <= 4:
        for k in range(min_page):
            display_page[k] = k+1
    elif now_page >= end_page-3:
        for k in range(min_page):
            display_page[k] = (end_page-7)+(k+1)
    else:
        for k in range(min_page):
            display_page[k] = (now_page-4) + (k+1)
    
    previous_page_chunk = now_page-7
    if previous_page_chunk < 1:
        previous_page_chunk = 1
    next_page_chunk = now_page+7
    if next_page_chunk > end_page:
        next_page_chunk = end_page
    if 4 <now_page:
        active_previous_page_chunk = True
    else:
        active_previous_page_chunk = False
    
    if now_page < (end_page-3):
        active_next_page_chunk = True
    else:
        active_next_page_chunk = False

    context = {
        'boards' : boards,
        'now_page' : now_page,
        'end_page' : end_page,
        'display_page' : display_page,
        'previous_page_chunk' : previous_page_chunk,
        'next_page_chunk' : next_page_chunk,
        'active_previous_page_chunk' : active_previous_page_chunk,
        'active_next_page_chunk' : active_next_page_chunk
    }
    return context