Module(
    body=[
        Import(
            names=[alias(name='base64', asname=None)],
        ),
        Import(
            names=[alias(name='binascii', asname=None)],
        ),
        ImportFrom(
            module='PIL',
            names=[
                alias(name='Image', asname=None),
                alias(name='ImageDraw', asname=None),
                alias(name='PngImagePlugin', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='tools', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='UserError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='TransactionCase', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestImage',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='Tests for the different image tools helpers.', kind=None),
                ),
                FunctionDef(
                    name='setUp',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='TestImage', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='setUp',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='bg_color',
                                    ctx=Store(),
                                ),
                            ],
                            value=Tuple(
                                elts=[
                                    Constant(value=135, kind=None),
                                    Constant(value=90, kind=None),
                                    Constant(value=123, kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='fill_color',
                                    ctx=Store(),
                                ),
                            ],
                            value=Tuple(
                                elts=[
                                    Constant(value=0, kind=None),
                                    Constant(value=160, kind=None),
                                    Constant(value=157, kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='base64_1x1_png',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=b'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAADElEQVR4nGNgYGAAAAAEAAH2FzhVAAAAAElFTkSuQmCC', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='base64_svg',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='base64', ctx=Load()),
                                    attr='b64encode',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=b'<svg></svg>', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='base64_1920x1080_jpeg',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='image_to_base64',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='Image', ctx=Load()),
                                            attr='new',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='RGB', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value=1920, kind=None),
                                                    Constant(value=1080, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='JPEG', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='base64_exif_jpg',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=b'/9j/4AAQSkZJRgABAQAAAQABAAD/4QDQRXhpZgAATU0AKgAAAAgABgESAAMAAAABAAYAAAEaAAUA\n                                  AAABAAAAVgEbAAUAAAABAAAAXgEoAAMAAAABAAEAAAITAAMAAAABAAEAAIdpAAQAAAABAAAAZgAA\n                                  AAAAAAABAAAAAQAAAAEAAAABAAWQAAAHAAAABDAyMzGRAQAHAAAABAECAwCgAAAHAAAABDAxMDCg\n                                  AQADAAAAAf//AACkMgAFAAAABAAAAKgAAAAAAAABjwAAAGQAAAGPAAAAZAAAAAkAAAAFAAAACQAA\n                                  AAX/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAx\n                                  NDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIy\n                                  MjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAADAAYDASIAAhEBAxEB/8QAHwAAAQUBAQEB\n                                  AQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1Fh\n                                  ByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZ\n                                  WmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXG\n                                  x8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAEC\n                                  AwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHB\n                                  CSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0\n                                  dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX\n                                  2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD3+iiigD//2Q==', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='image', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Image', ctx=Load()),
                                    attr='new',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='RGB', kind=None),
                                    Tuple(
                                        elts=[
                                            Constant(value=1920, kind=None),
                                            Constant(value=1080, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='color',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='bg_color',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='offset', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Subscript(
                                        value=Attribute(
                                            value=Name(id='image', ctx=Load()),
                                            attr='size',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    op=Sub(),
                                    right=Subscript(
                                        value=Attribute(
                                            value=Name(id='image', ctx=Load()),
                                            attr='size',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=1, kind=None),
                                        ctx=Load(),
                                    ),
                                ),
                                op=Div(),
                                right=Constant(value=2, kind=None),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='draw', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ImageDraw', ctx=Load()),
                                    attr='Draw',
                                    ctx=Load(),
                                ),
                                args=[Name(id='image', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='draw', ctx=Load()),
                                    attr='rectangle',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='xy',
                                        value=List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='offset', ctx=Load()),
                                                        Constant(value=0, kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                Tuple(
                                                    elts=[
                                                        BinOp(
                                                            left=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='image', ctx=Load()),
                                                                    attr='size',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            op=Sub(),
                                                            right=Name(id='offset', ctx=Load()),
                                                        ),
                                                        Subscript(
                                                            value=Attribute(
                                                                value=Name(id='image', ctx=Load()),
                                                                attr='size',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value=1, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='fill',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='fill_color',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='base64_1920x1080_png',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='image_to_base64',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='image', ctx=Load()),
                                    Constant(value='PNG', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='image', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Image', ctx=Load()),
                                    attr='new',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='RGB', kind=None),
                                    Tuple(
                                        elts=[
                                            Constant(value=1080, kind=None),
                                            Constant(value=1920, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='color',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='bg_color',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='offset', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Subscript(
                                        value=Attribute(
                                            value=Name(id='image', ctx=Load()),
                                            attr='size',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=1, kind=None),
                                        ctx=Load(),
                                    ),
                                    op=Sub(),
                                    right=Subscript(
                                        value=Attribute(
                                            value=Name(id='image', ctx=Load()),
                                            attr='size',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                ),
                                op=Div(),
                                right=Constant(value=2, kind=None),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='draw', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ImageDraw', ctx=Load()),
                                    attr='Draw',
                                    ctx=Load(),
                                ),
                                args=[Name(id='image', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='draw', ctx=Load()),
                                    attr='rectangle',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='xy',
                                        value=List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value=0, kind=None),
                                                        Name(id='offset', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                Tuple(
                                                    elts=[
                                                        Subscript(
                                                            value=Attribute(
                                                                value=Name(id='image', ctx=Load()),
                                                                attr='size',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        BinOp(
                                                            left=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='image', ctx=Load()),
                                                                    attr='size',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value=1, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            op=Sub(),
                                                            right=Name(id='offset', ctx=Load()),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='fill',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='fill_color',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='base64_1080x1920_png',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='image_to_base64',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='image', ctx=Load()),
                                    Constant(value='PNG', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_00_base64_to_image',
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
                        Expr(
                            value=Constant(value='Test that base64 is correctly opened as a PIL image.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='image', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='base64_to_image',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='base64_1x1_png',
                                        ctx=Load(),
                                    ),
                                ],
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
                                    Call(
                                        func=Name(id='type', ctx=Load()),
                                        args=[Name(id='image', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Name(id='PngImagePlugin', ctx=Load()),
                                        attr='PngImageFile',
                                        ctx=Load(),
                                    ),
                                    Constant(value='base64 as bytes, correct format', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='image', ctx=Load()),
                                        attr='size',
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value=1, kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(value='base64 as bytes, correct size', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='image', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='base64_to_image',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='base64_1x1_png',
                                                ctx=Load(),
                                            ),
                                            attr='decode',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='ASCII', kind=None)],
                                        keywords=[],
                                    ),
                                ],
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
                                    Call(
                                        func=Name(id='type', ctx=Load()),
                                        args=[Name(id='image', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Name(id='PngImagePlugin', ctx=Load()),
                                        attr='PngImageFile',
                                        ctx=Load(),
                                    ),
                                    Constant(value='base64 as string, correct format', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='image', ctx=Load()),
                                        attr='size',
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value=1, kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(value='base64 as string, correct size', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='UserError', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='msg',
                                                value=Constant(value='This file could not be decoded as an image file. Please try with a different file.', kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='image', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='base64_to_image',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=b'oazdazpodazdpok', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='UserError', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='msg',
                                                value=Constant(value='This file could not be decoded as an image file. Please try with a different file.', kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='image', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='base64_to_image',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=b'oazdazpodazdpokd', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_01_image_to_base64',
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
                        Expr(
                            value=Constant(value='Test that a PIL image is correctly saved as base64.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='image', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Image', ctx=Load()),
                                    attr='new',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='RGB', kind=None),
                                    Tuple(
                                        elts=[
                                            Constant(value=1, kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='image_base64', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='image_to_base64',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='image', ctx=Load()),
                                    Constant(value='PNG', kind=None),
                                ],
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
                                    Name(id='image_base64', ctx=Load()),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='base64_1x1_png',
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
                    name='test_02_image_fix_orientation',
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
                        Expr(
                            value=Constant(value='Test that the orientation of images is correct.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='blue', ctx=Store())],
                            value=Tuple(
                                elts=[
                                    Constant(value=0, kind=None),
                                    Constant(value=0, kind=None),
                                    Constant(value=255, kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='yellow', ctx=Store())],
                            value=Tuple(
                                elts=[
                                    Constant(value=255, kind=None),
                                    Constant(value=255, kind=None),
                                    Constant(value=0, kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='green', ctx=Store())],
                            value=Tuple(
                                elts=[
                                    Constant(value=0, kind=None),
                                    Constant(value=255, kind=None),
                                    Constant(value=0, kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='pink', ctx=Store())],
                            value=Tuple(
                                elts=[
                                    Constant(value=255, kind=None),
                                    Constant(value=0, kind=None),
                                    Constant(value=255, kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='size', ctx=Store())],
                            value=Constant(value=50, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=Tuple(
                                elts=[
                                    Name(id='blue', ctx=Load()),
                                    Name(id='yellow', ctx=Load()),
                                    Name(id='green', ctx=Load()),
                                    Name(id='pink', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_orientation_test',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=1, kind=None),
                                    Tuple(
                                        elts=[
                                            Name(id='blue', ctx=Load()),
                                            Name(id='yellow', ctx=Load()),
                                            Name(id='green', ctx=Load()),
                                            Name(id='pink', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='size', ctx=Load()),
                                    Name(id='expected', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_orientation_test',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=2, kind=None),
                                    Tuple(
                                        elts=[
                                            Name(id='yellow', ctx=Load()),
                                            Name(id='blue', ctx=Load()),
                                            Name(id='pink', ctx=Load()),
                                            Name(id='green', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='size', ctx=Load()),
                                    Name(id='expected', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_orientation_test',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=3, kind=None),
                                    Tuple(
                                        elts=[
                                            Name(id='pink', ctx=Load()),
                                            Name(id='green', ctx=Load()),
                                            Name(id='yellow', ctx=Load()),
                                            Name(id='blue', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='size', ctx=Load()),
                                    Name(id='expected', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_orientation_test',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=4, kind=None),
                                    Tuple(
                                        elts=[
                                            Name(id='green', ctx=Load()),
                                            Name(id='pink', ctx=Load()),
                                            Name(id='blue', ctx=Load()),
                                            Name(id='yellow', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='size', ctx=Load()),
                                    Name(id='expected', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_orientation_test',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=5, kind=None),
                                    Tuple(
                                        elts=[
                                            Name(id='blue', ctx=Load()),
                                            Name(id='green', ctx=Load()),
                                            Name(id='yellow', ctx=Load()),
                                            Name(id='pink', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='size', ctx=Load()),
                                    Name(id='expected', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_orientation_test',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=6, kind=None),
                                    Tuple(
                                        elts=[
                                            Name(id='yellow', ctx=Load()),
                                            Name(id='pink', ctx=Load()),
                                            Name(id='blue', ctx=Load()),
                                            Name(id='green', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='size', ctx=Load()),
                                    Name(id='expected', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_orientation_test',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=7, kind=None),
                                    Tuple(
                                        elts=[
                                            Name(id='pink', ctx=Load()),
                                            Name(id='yellow', ctx=Load()),
                                            Name(id='green', ctx=Load()),
                                            Name(id='blue', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='size', ctx=Load()),
                                    Name(id='expected', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_orientation_test',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=8, kind=None),
                                    Tuple(
                                        elts=[
                                            Name(id='green', ctx=Load()),
                                            Name(id='blue', ctx=Load()),
                                            Name(id='pink', ctx=Load()),
                                            Name(id='yellow', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='size', ctx=Load()),
                                    Name(id='expected', ctx=Load()),
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
                    name='test_03_image_fix_orientation_exif',
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
                        Expr(
                            value=Constant(value='Test that a jpg image with exif orientation tag gets rotated', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='image', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='base64_to_image',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='base64_exif_jpg',
                                        ctx=Load(),
                                    ),
                                ],
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
                                    Attribute(
                                        value=Name(id='image', ctx=Load()),
                                        attr='size',
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value=6, kind=None),
                                            Constant(value=3, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='image', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='image_fix_orientation',
                                    ctx=Load(),
                                ),
                                args=[Name(id='image', ctx=Load())],
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
                                    Attribute(
                                        value=Name(id='image', ctx=Load()),
                                        attr='size',
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value=3, kind=None),
                                            Constant(value=6, kind=None),
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
                    name='test_10_image_process_base64_source',
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
                        Expr(
                            value=Constant(value='Test the base64_source parameter of image_process.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='wrong_base64', ctx=Store())],
                            value=Constant(value=b'oazdazpodazdpok', kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='image_process',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=False, kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value='return False if base64_source is falsy', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='image_process',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='base64_svg',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='base64_svg',
                                        ctx=Load(),
                                    ),
                                    Constant(value='return base64_source if format is SVG', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='UserError', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='msg',
                                                value=Constant(value='This file could not be decoded as an image file. Please try with a different file.', kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='image_process',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='wrong_base64', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='quality',
                                                value=Constant(value=95, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='UserError', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='msg',
                                                value=Constant(value='This file could not be decoded as an image file. Please try with a different file.', kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='image_process',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=b'oazdazpodazdpokd', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='quality',
                                                value=Constant(value=95, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='image', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='base64_to_image',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='image_process',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='base64_1920x1080_jpeg',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='quality',
                                                value=Constant(value=95, kind=None),
                                            ),
                                        ],
                                    ),
                                ],
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
                                    Attribute(
                                        value=Name(id='image', ctx=Load()),
                                        attr='size',
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value=1920, kind=None),
                                            Constant(value=1080, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(value='OK return the image', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='image_process',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='wrong_base64', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Name(id='wrong_base64', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='image_process',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='wrong_base64', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='size',
                                                value=Constant(value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                    Name(id='wrong_base64', ctx=Load()),
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
                    name='test_11_image_process_size',
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
                        Expr(
                            value=Constant(value='Test the size parameter of image_process.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='tests', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='base64_1920x1080_jpeg',
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=192, kind=None),
                                                    Constant(value=108, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=192, kind=None),
                                                    Constant(value=108, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='resize to given size', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='base64_1920x1080_jpeg',
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=1920, kind=None),
                                                    Constant(value=1080, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=1920, kind=None),
                                                    Constant(value=1080, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='same size, no change', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='base64_1920x1080_jpeg',
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=192, kind=None),
                                                    Constant(value=None, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=192, kind=None),
                                                    Constant(value=108, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='set height from ratio', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='base64_1920x1080_jpeg',
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=0, kind=None),
                                                    Constant(value=108, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=192, kind=None),
                                                    Constant(value=108, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='set width from ratio', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='base64_1920x1080_jpeg',
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=192, kind=None),
                                                    Constant(value=200, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=192, kind=None),
                                                    Constant(value=108, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='adapt to width', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='base64_1920x1080_jpeg',
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=400, kind=None),
                                                    Constant(value=108, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=192, kind=None),
                                                    Constant(value=108, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='adapt to height', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='base64_1920x1080_jpeg',
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=3000, kind=None),
                                                    Constant(value=2000, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=1920, kind=None),
                                                    Constant(value=1080, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value="don't resize above original, both set", kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='base64_1920x1080_jpeg',
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=3000, kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=1920, kind=None),
                                                    Constant(value=1080, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value="don't resize above original, width set", kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='base64_1920x1080_jpeg',
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=None, kind=None),
                                                    Constant(value=2000, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=1920, kind=None),
                                                    Constant(value=1080, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value="don't resize above original, height set", kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='base64_1080x1920_png',
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=3000, kind=None),
                                                    Constant(value=192, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=108, kind=None),
                                                    Constant(value=192, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='vertical image, resize if below', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='count', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='test', ctx=Store()),
                            iter=Name(id='tests', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='image', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='base64_to_image',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='tools', ctx=Load()),
                                                    attr='image_process',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='test', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='size',
                                                        value=Subscript(
                                                            value=Name(id='test', ctx=Load()),
                                                            slice=Constant(value=1, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
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
                                            Attribute(
                                                value=Name(id='image', ctx=Load()),
                                                attr='size',
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='test', ctx=Load()),
                                                slice=Constant(value=2, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='test', ctx=Load()),
                                                slice=Constant(value=3, kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='count', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='count', ctx=Load()),
                                        op=Add(),
                                        right=Constant(value=1, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
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
                                    Name(id='count', ctx=Load()),
                                    Constant(value=10, kind=None),
                                    Constant(value='ensure the loop is ran', kind=None),
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
                    name='test_12_image_process_verify_resolution',
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
                        Expr(
                            value=Constant(value='Test the verify_resolution parameter of image_process.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='image_process',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='base64_1920x1080_jpeg',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='verify_resolution',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertNotEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='res', ctx=Load()),
                                    Constant(value=False, kind=None),
                                    Constant(value='size ok', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='base64_image_excessive', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='image_to_base64',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='Image', ctx=Load()),
                                            attr='new',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='RGB', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value=45001, kind=None),
                                                    Constant(value=1000, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='PNG', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='ValueError', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='msg',
                                                value=Constant(value='size excessive', kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='image_process',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='base64_image_excessive', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='verify_resolution',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_13_image_process_quality',
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
                        Expr(
                            value=Constant(value='Test the quality parameter of image_process.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='image', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='image_to_base64',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='Image', ctx=Load()),
                                            attr='new',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='RGBA', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value=1080, kind=None),
                                                    Constant(value=1920, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='PNG', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='image_process',
                                    ctx=Load(),
                                ),
                                args=[Name(id='image', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertLessEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='res', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='image', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='image', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='image_to_base64',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='Image', ctx=Load()),
                                            attr='new',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='P', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value=1080, kind=None),
                                                    Constant(value=1920, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='PNG', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='image_process',
                                    ctx=Load(),
                                ),
                                args=[Name(id='image', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertLessEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='res', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='image', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='image_process',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='base64_1920x1080_jpeg',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertLessEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='res', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='base64_1920x1080_jpeg',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='image', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='image_to_base64',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='Image', ctx=Load()),
                                            attr='new',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='RGB', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value=1080, kind=None),
                                                    Constant(value=1920, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='GIF', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='image_process',
                                    ctx=Load(),
                                ),
                                args=[Name(id='image', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertLessEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='res', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='image', ctx=Load())],
                                        keywords=[],
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
                    name='test_14_image_process_crop',
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
                        Expr(
                            value=Constant(value='Test the crop parameter of image_process.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='fill', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='bg', ctx=Store())],
                            value=Constant(value=1, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tests', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='base64_1920x1080_png',
                                                ctx=Load(),
                                            ),
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value=1920, kind=None),
                                                    Constant(value=1080, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Name(id='fill', ctx=Load()),
                                                    Name(id='fill', ctx=Load()),
                                                    Name(id='bg', ctx=Load()),
                                                    Name(id='bg', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='horizontal, verify initial', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='base64_1920x1080_png',
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=2000, kind=None),
                                                    Constant(value=2000, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='center', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value=1080, kind=None),
                                                    Constant(value=1080, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Name(id='fill', ctx=Load()),
                                                    Name(id='fill', ctx=Load()),
                                                    Name(id='fill', ctx=Load()),
                                                    Name(id='fill', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='horizontal, crop biggest possible', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='base64_1920x1080_png',
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=2000, kind=None),
                                                    Constant(value=4000, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='center', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value=540, kind=None),
                                                    Constant(value=1080, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Name(id='fill', ctx=Load()),
                                                    Name(id='fill', ctx=Load()),
                                                    Name(id='fill', ctx=Load()),
                                                    Name(id='fill', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='horizontal, size vertical, limit height', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='base64_1920x1080_png',
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=4000, kind=None),
                                                    Constant(value=2000, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='center', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value=1920, kind=None),
                                                    Constant(value=960, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Name(id='fill', ctx=Load()),
                                                    Name(id='fill', ctx=Load()),
                                                    Name(id='bg', ctx=Load()),
                                                    Name(id='bg', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='horizontal, size horizontal, limit width', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='base64_1920x1080_png',
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=512, kind=None),
                                                    Constant(value=512, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='center', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value=512, kind=None),
                                                    Constant(value=512, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Name(id='fill', ctx=Load()),
                                                    Name(id='fill', ctx=Load()),
                                                    Name(id='fill', ctx=Load()),
                                                    Name(id='fill', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='horizontal, type center', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='base64_1920x1080_png',
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=512, kind=None),
                                                    Constant(value=512, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='top', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value=512, kind=None),
                                                    Constant(value=512, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Name(id='fill', ctx=Load()),
                                                    Name(id='fill', ctx=Load()),
                                                    Name(id='fill', ctx=Load()),
                                                    Name(id='fill', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='horizontal, type top', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='base64_1920x1080_png',
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=512, kind=None),
                                                    Constant(value=512, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='bottom', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value=512, kind=None),
                                                    Constant(value=512, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Name(id='fill', ctx=Load()),
                                                    Name(id='fill', ctx=Load()),
                                                    Name(id='fill', ctx=Load()),
                                                    Name(id='fill', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='horizontal, type bottom', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='base64_1920x1080_png',
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=512, kind=None),
                                                    Constant(value=512, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='wrong', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value=512, kind=None),
                                                    Constant(value=512, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Name(id='fill', ctx=Load()),
                                                    Name(id='fill', ctx=Load()),
                                                    Name(id='fill', ctx=Load()),
                                                    Name(id='fill', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='horizontal, wrong crop value, use center', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='base64_1920x1080_png',
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=192, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value=None, kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value=192, kind=None),
                                                    Constant(value=108, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Name(id='fill', ctx=Load()),
                                                    Name(id='fill', ctx=Load()),
                                                    Name(id='bg', ctx=Load()),
                                                    Name(id='bg', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='horizontal, not cropped, just do resize', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='base64_1080x1920_png',
                                                ctx=Load(),
                                            ),
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value=1080, kind=None),
                                                    Constant(value=1920, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Name(id='bg', ctx=Load()),
                                                    Name(id='bg', ctx=Load()),
                                                    Name(id='fill', ctx=Load()),
                                                    Name(id='fill', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='vertical, verify initial', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='base64_1080x1920_png',
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=2000, kind=None),
                                                    Constant(value=2000, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='center', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value=1080, kind=None),
                                                    Constant(value=1080, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Name(id='fill', ctx=Load()),
                                                    Name(id='fill', ctx=Load()),
                                                    Name(id='fill', ctx=Load()),
                                                    Name(id='fill', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='vertical, crop biggest possible', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='base64_1080x1920_png',
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=2000, kind=None),
                                                    Constant(value=4000, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='center', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value=960, kind=None),
                                                    Constant(value=1920, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Name(id='bg', ctx=Load()),
                                                    Name(id='bg', ctx=Load()),
                                                    Name(id='fill', ctx=Load()),
                                                    Name(id='fill', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='vertical, size vertical, limit height', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='base64_1080x1920_png',
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=4000, kind=None),
                                                    Constant(value=2000, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='center', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value=1080, kind=None),
                                                    Constant(value=540, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Name(id='fill', ctx=Load()),
                                                    Name(id='fill', ctx=Load()),
                                                    Name(id='fill', ctx=Load()),
                                                    Name(id='fill', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='vertical, size horizontal, limit width', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='base64_1080x1920_png',
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=512, kind=None),
                                                    Constant(value=512, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='center', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value=512, kind=None),
                                                    Constant(value=512, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Name(id='fill', ctx=Load()),
                                                    Name(id='fill', ctx=Load()),
                                                    Name(id='fill', ctx=Load()),
                                                    Name(id='fill', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='vertical, type center', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='base64_1080x1920_png',
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=512, kind=None),
                                                    Constant(value=512, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='top', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value=512, kind=None),
                                                    Constant(value=512, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Name(id='bg', ctx=Load()),
                                                    Name(id='fill', ctx=Load()),
                                                    Name(id='fill', ctx=Load()),
                                                    Name(id='fill', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='vertical, type top', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='base64_1080x1920_png',
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=512, kind=None),
                                                    Constant(value=512, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='bottom', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value=512, kind=None),
                                                    Constant(value=512, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Name(id='fill', ctx=Load()),
                                                    Name(id='bg', ctx=Load()),
                                                    Name(id='fill', ctx=Load()),
                                                    Name(id='fill', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='vertical, type bottom', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='base64_1080x1920_png',
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=512, kind=None),
                                                    Constant(value=512, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='wrong', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value=512, kind=None),
                                                    Constant(value=512, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Name(id='fill', ctx=Load()),
                                                    Name(id='fill', ctx=Load()),
                                                    Name(id='fill', ctx=Load()),
                                                    Name(id='fill', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='vertical, wrong crop value, use center', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='base64_1080x1920_png',
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=108, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value=None, kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value=108, kind=None),
                                                    Constant(value=192, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Name(id='bg', ctx=Load()),
                                                    Name(id='bg', ctx=Load()),
                                                    Name(id='fill', ctx=Load()),
                                                    Name(id='fill', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='vertical, not cropped, just do resize', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='count', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='test', ctx=Store()),
                            iter=Name(id='tests', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='count', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='count', ctx=Load()),
                                        op=Add(),
                                        right=Constant(value=1, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='image', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='base64_to_image',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='tools', ctx=Load()),
                                                    attr='image_process',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='test', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='size',
                                                        value=Subscript(
                                                            value=Name(id='test', ctx=Load()),
                                                            slice=Constant(value=1, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='crop',
                                                        value=Subscript(
                                                            value=Name(id='test', ctx=Load()),
                                                            slice=Constant(value=2, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='quality',
                                                        value=Constant(value=95, kind=None),
                                                    ),
                                                ],
                                            ),
                                        ],
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
                                            Attribute(
                                                value=Name(id='image', ctx=Load()),
                                                attr='size',
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='test', ctx=Load()),
                                                slice=Constant(value=3, kind=None),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Constant(value='%s - correct size', kind=None),
                                                op=Mod(),
                                                right=Subscript(
                                                    value=Name(id='test', ctx=Load()),
                                                    slice=Constant(value=5, kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='half_width', ctx=Store()),
                                                Name(id='half_height', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Tuple(
                                        elts=[
                                            BinOp(
                                                left=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='image', ctx=Load()),
                                                        attr='size',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                op=Div(),
                                                right=Constant(value=2, kind=None),
                                            ),
                                            BinOp(
                                                left=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='image', ctx=Load()),
                                                        attr='size',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=1, kind=None),
                                                    ctx=Load(),
                                                ),
                                                op=Div(),
                                                right=Constant(value=2, kind=None),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='top', ctx=Store()),
                                                Name(id='bottom', ctx=Store()),
                                                Name(id='left', ctx=Store()),
                                                Name(id='right', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Tuple(
                                        elts=[
                                            Constant(value=0, kind=None),
                                            BinOp(
                                                left=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='image', ctx=Load()),
                                                        attr='size',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=1, kind=None),
                                                    ctx=Load(),
                                                ),
                                                op=Sub(),
                                                right=Constant(value=1, kind=None),
                                            ),
                                            Constant(value=0, kind=None),
                                            BinOp(
                                                left=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='image', ctx=Load()),
                                                        attr='size',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                op=Sub(),
                                                right=Constant(value=1, kind=None),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='px', ctx=Store())],
                                    value=Tuple(
                                        elts=[
                                            Name(id='half_width', ctx=Load()),
                                            Name(id='top', ctx=Load()),
                                        ],
                                        ctx=Load(),
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
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='image', ctx=Load()),
                                                    attr='getpixel',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='px', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Subscript(
                                                value=Subscript(
                                                    value=Name(id='test', ctx=Load()),
                                                    slice=Constant(value=4, kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Constant(value='%s - color top (%s, %s)', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Subscript(
                                                            value=Name(id='test', ctx=Load()),
                                                            slice=Constant(value=5, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        Subscript(
                                                            value=Name(id='px', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        Subscript(
                                                            value=Name(id='px', ctx=Load()),
                                                            slice=Constant(value=1, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='px', ctx=Store())],
                                    value=Tuple(
                                        elts=[
                                            Name(id='half_width', ctx=Load()),
                                            Name(id='bottom', ctx=Load()),
                                        ],
                                        ctx=Load(),
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
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='image', ctx=Load()),
                                                    attr='getpixel',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='px', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Subscript(
                                                value=Subscript(
                                                    value=Name(id='test', ctx=Load()),
                                                    slice=Constant(value=4, kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Constant(value='%s - color bottom (%s, %s)', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Subscript(
                                                            value=Name(id='test', ctx=Load()),
                                                            slice=Constant(value=5, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        Subscript(
                                                            value=Name(id='px', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        Subscript(
                                                            value=Name(id='px', ctx=Load()),
                                                            slice=Constant(value=1, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='px', ctx=Store())],
                                    value=Tuple(
                                        elts=[
                                            Name(id='left', ctx=Load()),
                                            Name(id='half_height', ctx=Load()),
                                        ],
                                        ctx=Load(),
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
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='image', ctx=Load()),
                                                    attr='getpixel',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='px', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Subscript(
                                                value=Subscript(
                                                    value=Name(id='test', ctx=Load()),
                                                    slice=Constant(value=4, kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=2, kind=None),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Constant(value='%s - color left (%s, %s)', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Subscript(
                                                            value=Name(id='test', ctx=Load()),
                                                            slice=Constant(value=5, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        Subscript(
                                                            value=Name(id='px', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        Subscript(
                                                            value=Name(id='px', ctx=Load()),
                                                            slice=Constant(value=1, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='px', ctx=Store())],
                                    value=Tuple(
                                        elts=[
                                            Name(id='right', ctx=Load()),
                                            Name(id='half_height', ctx=Load()),
                                        ],
                                        ctx=Load(),
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
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='image', ctx=Load()),
                                                    attr='getpixel',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='px', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Subscript(
                                                value=Subscript(
                                                    value=Name(id='test', ctx=Load()),
                                                    slice=Constant(value=4, kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=3, kind=None),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Constant(value='%s - color right (%s, %s)', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Subscript(
                                                            value=Name(id='test', ctx=Load()),
                                                            slice=Constant(value=5, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        Subscript(
                                                            value=Name(id='px', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        Subscript(
                                                            value=Name(id='px', ctx=Load()),
                                                            slice=Constant(value=1, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
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
                                    Name(id='count', ctx=Load()),
                                    BinOp(
                                        left=Constant(value=2, kind=None),
                                        op=Mult(),
                                        right=Constant(value=9, kind=None),
                                    ),
                                    Constant(value='ensure the loop is ran', kind=None),
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
                    name='test_15_image_process_colorize',
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
                        Expr(
                            value=Constant(value='Test the colorize parameter of image_process.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='image_rgba', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Image', ctx=Load()),
                                    attr='new',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='RGBA', kind=None),
                                    Tuple(
                                        elts=[
                                            Constant(value=1, kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
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
                                    Attribute(
                                        value=Name(id='image_rgba', ctx=Load()),
                                        attr='mode',
                                        ctx=Load(),
                                    ),
                                    Constant(value='RGBA', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='image_rgba', ctx=Load()),
                                            attr='getpixel',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='base64_rgba', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='image_to_base64',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='image_rgba', ctx=Load()),
                                    Constant(value='PNG', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='image', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='base64_to_image',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='image_process',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='base64_rgba', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='colorize',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                ],
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
                                    Attribute(
                                        value=Name(id='image', ctx=Load()),
                                        attr='mode',
                                        ctx=Load(),
                                    ),
                                    Constant(value='RGB', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertNotEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='image', ctx=Load()),
                                            attr='getpixel',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
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
                    name='test_16_image_process_format',
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
                        Expr(
                            value=Constant(value='Test the format parameter of image_process.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='image', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='base64_to_image',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='image_process',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='base64_1920x1080_jpeg',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='output_format',
                                                value=Constant(value='PNG', kind=None),
                                            ),
                                        ],
                                    ),
                                ],
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
                                    Attribute(
                                        value=Name(id='image', ctx=Load()),
                                        attr='format',
                                        ctx=Load(),
                                    ),
                                    Constant(value='PNG', kind=None),
                                    Constant(value='change format to PNG', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='image', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='base64_to_image',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='image_process',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='base64_1x1_png',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='output_format',
                                                value=Constant(value='JpEg', kind=None),
                                            ),
                                        ],
                                    ),
                                ],
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
                                    Attribute(
                                        value=Name(id='image', ctx=Load()),
                                        attr='format',
                                        ctx=Load(),
                                    ),
                                    Constant(value='JPEG', kind=None),
                                    Constant(value='change format to JPEG (case insensitive)', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='image', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='base64_to_image',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='image_process',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='base64_1920x1080_jpeg',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='output_format',
                                                value=Constant(value='BMP', kind=None),
                                            ),
                                        ],
                                    ),
                                ],
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
                                    Attribute(
                                        value=Name(id='image', ctx=Load()),
                                        attr='format',
                                        ctx=Load(),
                                    ),
                                    Constant(value='PNG', kind=None),
                                    Constant(value='change format to BMP converted to PNG', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='base64_image_1080_1920_rgba',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='image_to_base64',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='Image', ctx=Load()),
                                            attr='new',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='RGBA', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value=108, kind=None),
                                                    Constant(value=192, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='PNG', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='image', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='base64_to_image',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='image_process',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='base64_image_1080_1920_rgba',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='output_format',
                                                value=Constant(value='jpeg', kind=None),
                                            ),
                                        ],
                                    ),
                                ],
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
                                    Attribute(
                                        value=Name(id='image', ctx=Load()),
                                        attr='format',
                                        ctx=Load(),
                                    ),
                                    Constant(value='JPEG', kind=None),
                                    Constant(value='change format PNG with RGBA to JPEG', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='base64_image_1080_1920_tiff',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='image_to_base64',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='Image', ctx=Load()),
                                            attr='new',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='RGB', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value=108, kind=None),
                                                    Constant(value=192, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='TIFF', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='image', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='base64_to_image',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='image_process',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='base64_image_1080_1920_tiff',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='quality',
                                                value=Constant(value=95, kind=None),
                                            ),
                                        ],
                                    ),
                                ],
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
                                    Attribute(
                                        value=Name(id='image', ctx=Load()),
                                        attr='format',
                                        ctx=Load(),
                                    ),
                                    Constant(value='JPEG', kind=None),
                                    Constant(value='unsupported format to JPEG', kind=None),
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
                    name='test_20_image_data_uri',
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
                        Expr(
                            value=Constant(value='Test that image_data_uri is working as expected.', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='image_data_uri',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='base64_1x1_png',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    BinOp(
                                        left=Constant(value='data:image/png;base64,', kind=None),
                                        op=Add(),
                                        right=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='base64_1x1_png',
                                                    ctx=Load(),
                                                ),
                                                attr='decode',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='ascii', kind=None)],
                                            keywords=[],
                                        ),
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
                    name='_assertAlmostEqualSequence',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='rgb1', annotation=None, type_comment=None),
                            arg(arg='rgb2', annotation=None, type_comment=None),
                            arg(arg='delta', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=10, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='rgb1', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='rgb2', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='index', ctx=Store()),
                                    Name(id='t', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='enumerate', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='zip', ctx=Load()),
                                        args=[
                                            Name(id='rgb1', ctx=Load()),
                                            Name(id='rgb2', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertAlmostEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='t', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='t', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='delta',
                                                value=Name(id='delta', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='msg',
                                                value=BinOp(
                                                    left=Constant(value='%s vs %s at %d', kind=None),
                                                    op=Mod(),
                                                    right=Tuple(
                                                        elts=[
                                                            Name(id='rgb1', ctx=Load()),
                                                            Name(id='rgb2', ctx=Load()),
                                                            Name(id='index', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_exif_colored_square_b64',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='orientation', annotation=None, type_comment=None),
                            arg(arg='colors', annotation=None, type_comment=None),
                            arg(arg='size', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='image', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Image', ctx=Load()),
                                    attr='new',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='RGB', kind=None),
                                    Tuple(
                                        elts=[
                                            Name(id='size', ctx=Load()),
                                            Name(id='size', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='color',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='bg_color',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='draw', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ImageDraw', ctx=Load()),
                                    attr='Draw',
                                    ctx=Load(),
                                ),
                                args=[Name(id='image', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='draw', ctx=Load()),
                                    attr='rectangle',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='xy',
                                        value=List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value=0, kind=None),
                                                        Constant(value=0, kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                Tuple(
                                                    elts=[
                                                        BinOp(
                                                            left=Name(id='size', ctx=Load()),
                                                            op=FloorDiv(),
                                                            right=Constant(value=2, kind=None),
                                                        ),
                                                        BinOp(
                                                            left=Name(id='size', ctx=Load()),
                                                            op=FloorDiv(),
                                                            right=Constant(value=2, kind=None),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='fill',
                                        value=Subscript(
                                            value=Name(id='colors', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='draw', ctx=Load()),
                                    attr='rectangle',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='xy',
                                        value=List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        BinOp(
                                                            left=Name(id='size', ctx=Load()),
                                                            op=FloorDiv(),
                                                            right=Constant(value=2, kind=None),
                                                        ),
                                                        Constant(value=0, kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                Tuple(
                                                    elts=[
                                                        Name(id='size', ctx=Load()),
                                                        BinOp(
                                                            left=Name(id='size', ctx=Load()),
                                                            op=FloorDiv(),
                                                            right=Constant(value=2, kind=None),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='fill',
                                        value=Subscript(
                                            value=Name(id='colors', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='draw', ctx=Load()),
                                    attr='rectangle',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='xy',
                                        value=List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value=0, kind=None),
                                                        BinOp(
                                                            left=Name(id='size', ctx=Load()),
                                                            op=FloorDiv(),
                                                            right=Constant(value=2, kind=None),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                Tuple(
                                                    elts=[
                                                        BinOp(
                                                            left=Name(id='size', ctx=Load()),
                                                            op=FloorDiv(),
                                                            right=Constant(value=2, kind=None),
                                                        ),
                                                        Name(id='size', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='fill',
                                        value=Subscript(
                                            value=Name(id='colors', ctx=Load()),
                                            slice=Constant(value=2, kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='draw', ctx=Load()),
                                    attr='rectangle',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='xy',
                                        value=List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        BinOp(
                                                            left=Name(id='size', ctx=Load()),
                                                            op=FloorDiv(),
                                                            right=Constant(value=2, kind=None),
                                                        ),
                                                        BinOp(
                                                            left=Name(id='size', ctx=Load()),
                                                            op=FloorDiv(),
                                                            right=Constant(value=2, kind=None),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                Tuple(
                                                    elts=[
                                                        Name(id='size', ctx=Load()),
                                                        Name(id='size', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='fill',
                                        value=Subscript(
                                            value=Name(id='colors', ctx=Load()),
                                            slice=Constant(value=3, kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='exif', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Constant(value=b'Exif\x00\x00II*\x00\x08\x00\x00\x00\x01\x00\x12\x01\x03\x00\x01\x00\x00\x00', kind=None),
                                    op=Add(),
                                    right=Call(
                                        func=Name(id='bytes', ctx=Load()),
                                        args=[
                                            List(
                                                elts=[Name(id='orientation', ctx=Load())],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                op=Add(),
                                right=Constant(value=b'\x00\x00\x00\x00\x00\x00\x00', kind=None),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='image_to_base64',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='image', ctx=Load()),
                                    Constant(value='JPEG', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='exif',
                                        value=Name(id='exif', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_orientation_test',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='orientation', annotation=None, type_comment=None),
                            arg(arg='colors', annotation=None, type_comment=None),
                            arg(arg='size', annotation=None, type_comment=None),
                            arg(arg='expected', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='b64_image', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_exif_colored_square_b64',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='orientation', ctx=Load()),
                                    Name(id='colors', ctx=Load()),
                                    Name(id='size', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='fixed_image', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='image_fix_orientation',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='base64_to_image',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='b64_image', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_assertAlmostEqualSequence',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='fixed_image', ctx=Load()),
                                            attr='getpixel',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Subscript(
                                        value=Name(id='expected', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_assertAlmostEqualSequence',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='fixed_image', ctx=Load()),
                                            attr='getpixel',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Tuple(
                                                elts=[
                                                    BinOp(
                                                        left=Name(id='size', ctx=Load()),
                                                        op=Sub(),
                                                        right=Constant(value=1, kind=None),
                                                    ),
                                                    Constant(value=0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Subscript(
                                        value=Name(id='expected', ctx=Load()),
                                        slice=Constant(value=1, kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_assertAlmostEqualSequence',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='fixed_image', ctx=Load()),
                                            attr='getpixel',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=0, kind=None),
                                                    BinOp(
                                                        left=Name(id='size', ctx=Load()),
                                                        op=Sub(),
                                                        right=Constant(value=1, kind=None),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Subscript(
                                        value=Name(id='expected', ctx=Load()),
                                        slice=Constant(value=2, kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_assertAlmostEqualSequence',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='fixed_image', ctx=Load()),
                                            attr='getpixel',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Tuple(
                                                elts=[
                                                    BinOp(
                                                        left=Name(id='size', ctx=Load()),
                                                        op=Sub(),
                                                        right=Constant(value=1, kind=None),
                                                    ),
                                                    BinOp(
                                                        left=Name(id='size', ctx=Load()),
                                                        op=Sub(),
                                                        right=Constant(value=1, kind=None),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Subscript(
                                        value=Name(id='expected', ctx=Load()),
                                        slice=Constant(value=3, kind=None),
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
