Module(
    body=[
        Import(
            names=[alias(name='base64', asname=None)],
        ),
        Import(
            names=[alias(name='unittest', asname=None)],
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='BaseCase', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.mimetypes',
            names=[alias(name='guess_mimetype', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='PNG', ctx=Store())],
            value=Constant(value=b'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAADElEQVQI12P4//8/AAX+Av7czFnnAAAAAElFTkSuQmCC', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='GIF', ctx=Store())],
            value=Constant(value=b'R0lGODdhAQABAIAAAP///////ywAAAAAAQABAAACAkQBADs=', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='BMP', ctx=Store())],
            value=Constant(value=b'Qk1+AAAAAAAAAHoAAABsAAAAAQAAAAEAAAABABgAAAAAAAQAAAATCwAAEwsAAAAAAAAAAAAAQkdScwAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAD///8A', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='JPG', ctx=Store())],
            value=Constant(value='/9j/4AAQSkZJRgABAQEASABIAAD//gATQ3JlYXRlZCB3aXRoIEdJTVD/2wBDAP\n//////////////////////////////////////////////////////////////////////////////////////2wBDAf///////\n///////////////////////////////////////////////////////////////////////////////wgARCAABAAEDAREAAhEB\nAxEB/8QAFAABAAAAAAAAAAAAAAAAAAAAAv/EABQBAQAAAAAAAAAAAAAAAAAAAAD/2gAMAwEAAhADEAAAAUf/xAAUEAEAAAAAAAA\nAAAAAAAAAAAAA/9oACAEBAAEFAn//xAAUEQEAAAAAAAAAAAAAAAAAAAAA/9oACAEDAQE/AX//xAAUEQEAAAAAAAAAAAAAAAAAAA\nAA/9oACAECAQE/AX//xAAUEAEAAAAAAAAAAAAAAAAAAAAA/9oACAEBAAY/An//xAAUEAEAAAAAAAAAAAAAAAAAAAAA/9oACAEBA\nAE/IX//2gAMAwEAAgADAAAAEB//xAAUEQEAAAAAAAAAAAAAAAAAAAAA/9oACAEDAQE/EH//xAAUEQEAAAAAAAAAAAAAAAAAAAAA\n/9oACAECAQE/EH//xAAUEAEAAAAAAAAAAAAAAAAAAAAA/9oACAEBAAE/EH//2Q==', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='SVG', ctx=Store())],
            value=Constant(value=b'PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iaXNvLTg4NTktMSI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMjAwMDExMDIvL0VOIlxuICJodHRwOi8vd3d3LnczLm9yZy9UUi8yMDAwL0NSLVNWRy0yMDAwMTEwMi9EVEQvc3ZnLTIwMDAxMTAyLmR0ZCI+PHN2ZyB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSg1MCw1MCkiPjxyZWN0IHg9IjAiIHk9IjAiIHdpZHRoPSIxNTAiIGhlaWdodD0iNTAiIHN0eWxlPSJmaWxsOnJlZDsiIC8+PC9nPjwvc3ZnPg==', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='ZIP', ctx=Store())],
            value=Constant(value=b'UEsDBBQACAAIAGFva1AAAAAAAAAAAAAAAAAFACAAdC50eHRVVA0AB5bgaF6W4GheluBoXnV4CwABBOgDAAAE6AMAAA\nMAUEsHCAAAAAACAAAAAAAAAFBLAQIUAxQACAAIAGFva1AAAAAAAgAAAAAAAAAFACAAAAAAAAAAAACkgQAAAAB0LnR4dFVUDQAHlu\nBoXpbgaF6W4GhedXgLAAEE6AMAAAToAwAAUEsFBgAAAAABAAEAUwAAAFUAAAAAAA==', kind=None),
            type_comment=None,
        ),
        ClassDef(
            name='test_guess_mimetype',
            bases=[Name(id='BaseCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_default_mimetype_empty',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='mimetype', ctx=Store())],
                            value=Call(
                                func=Name(id='guess_mimetype', ctx=Load()),
                                args=[Constant(value=b'', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='mimetype', ctx=Load()),
                                    Tuple(
                                        elts=[
                                            Constant(value='application/octet-stream', kind=None),
                                            Constant(value='application/x-empty', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_default_mimetype',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='mimetype', ctx=Store())],
                            value=Call(
                                func=Name(id='guess_mimetype', ctx=Load()),
                                args=[Constant(value=b'', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='default',
                                        value=Constant(value='test', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='mimetype', ctx=Load()),
                                    Tuple(
                                        elts=[
                                            Constant(value='test', kind=None),
                                            Constant(value='application/x-empty', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_mimetype_octet_stream',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='mimetype', ctx=Store())],
                            value=Call(
                                func=Name(id='guess_mimetype', ctx=Load()),
                                args=[Constant(value=b'\x00', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='mimetype', ctx=Load()),
                                    Constant(value='application/octet-stream', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_mimetype_png',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='content', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='base64', ctx=Load()),
                                    attr='b64decode',
                                    ctx=Load(),
                                ),
                                args=[Name(id='PNG', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mimetype', ctx=Store())],
                            value=Call(
                                func=Name(id='guess_mimetype', ctx=Load()),
                                args=[Name(id='content', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='default',
                                        value=Constant(value='test', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='mimetype', ctx=Load()),
                                    Constant(value='image/png', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_mimetype_bmp',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='content', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='base64', ctx=Load()),
                                    attr='b64decode',
                                    ctx=Load(),
                                ),
                                args=[Name(id='BMP', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mimetype', ctx=Store())],
                            value=Call(
                                func=Name(id='guess_mimetype', ctx=Load()),
                                args=[Name(id='content', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='default',
                                        value=Constant(value='test', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertRegex',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='mimetype', ctx=Load()),
                                    Constant(value='image/.*\\bbmp', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_mimetype_jpg',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='content', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='base64', ctx=Load()),
                                    attr='b64decode',
                                    ctx=Load(),
                                ),
                                args=[Name(id='JPG', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mimetype', ctx=Store())],
                            value=Call(
                                func=Name(id='guess_mimetype', ctx=Load()),
                                args=[Name(id='content', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='default',
                                        value=Constant(value='test', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='mimetype', ctx=Load()),
                                    Constant(value='image/jpeg', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_mimetype_gif',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='content', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='base64', ctx=Load()),
                                    attr='b64decode',
                                    ctx=Load(),
                                ),
                                args=[Name(id='GIF', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mimetype', ctx=Store())],
                            value=Call(
                                func=Name(id='guess_mimetype', ctx=Load()),
                                args=[Name(id='content', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='default',
                                        value=Constant(value='test', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='mimetype', ctx=Load()),
                                    Constant(value='image/gif', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_mimetype_svg',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='content', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='base64', ctx=Load()),
                                    attr='b64decode',
                                    ctx=Load(),
                                ),
                                args=[Name(id='SVG', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mimetype', ctx=Store())],
                            value=Call(
                                func=Name(id='guess_mimetype', ctx=Load()),
                                args=[Name(id='content', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='default',
                                        value=Constant(value='test', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='mimetype', ctx=Load()),
                                            attr='startswith',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='image/svg', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='mimetype', ctx=Store())],
                            value=Call(
                                func=Name(id='guess_mimetype', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Constant(value=b'   ', kind=None),
                                        op=Add(),
                                        right=Name(id='content', ctx=Load()),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='default',
                                        value=Constant(value='test', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertNotIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='svg', kind=None),
                                    Name(id='mimetype', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_mimetype_zip',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='content', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='base64', ctx=Load()),
                                    attr='b64decode',
                                    ctx=Load(),
                                ),
                                args=[Name(id='ZIP', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mimetype', ctx=Store())],
                            value=Call(
                                func=Name(id='guess_mimetype', ctx=Load()),
                                args=[Name(id='content', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='default',
                                        value=Constant(value='test', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='mimetype', ctx=Load()),
                                    Constant(value='application/zip', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        If(
            test=Compare(
                left=Name(id='__name__', ctx=Load()),
                ops=[Eq()],
                comparators=[Constant(value='__main__', kind=None)],
            ),
            body=[
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='unittest', ctx=Load()),
                            attr='main',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                ),
            ],
            orelse=[],
        ),
    ],
    type_ignores=[],
)
