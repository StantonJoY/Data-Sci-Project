Module(
    body=[
        Import(
            names=[alias(name='base64', asname=None)],
        ),
        Import(
            names=[alias(name='hashlib', asname=None)],
        ),
        Import(
            names=[alias(name='io', asname=None)],
        ),
        Import(
            names=[alias(name='itertools', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='mimetypes', asname=None)],
        ),
        Import(
            names=[alias(name='os', asname=None)],
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        Import(
            names=[alias(name='uuid', asname=None)],
        ),
        ImportFrom(
            module='collections',
            names=[alias(name='defaultdict', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='PIL',
            names=[alias(name='Image', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='tools', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[
                alias(name='AccessError', asname=None),
                alias(name='ValidationError', asname=None),
                alias(name='MissingError', asname=None),
                alias(name='UserError', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='config', asname=None),
                alias(name='human_size', asname=None),
                alias(name='ustr', asname=None),
                alias(name='html_escape', asname=None),
                alias(name='ImageProcess', asname=None),
                alias(name='str2bool', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.mimetypes',
            names=[alias(name='guess_mimetype', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.osv',
            names=[alias(name='expression', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='_logger', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='logging', ctx=Load()),
                    attr='getLogger',
                    ctx=Load(),
                ),
                args=[Name(id='__name__', ctx=Load())],
                keywords=[],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='IrAttachment',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='Attachments are used to link binary files or url to any openerp document.\n\n    External attachment storage\n    ---------------------------\n\n    The computed field ``datas`` is implemented using ``_file_read``,\n    ``_file_write`` and ``_file_delete``, which can be overridden to implement\n    other storage engines. Such methods should check for other location pseudo\n    uri (example: hdfs://hadoopserver).\n\n    The default implementation is the file:dirname location that stores files\n    on the local filesystem using name based on their sha1 hash\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='ir.attachment', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Attachment', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_order', ctx=Store())],
                    value=Constant(value='id desc', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_res_name',
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
                        For(
                            target=Name(id='attachment', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='attachment', ctx=Load()),
                                                attr='res_model',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='attachment', ctx=Load()),
                                                attr='res_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='record', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Attribute(
                                                            value=Name(id='attachment', ctx=Load()),
                                                            attr='res_model',
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='attachment', ctx=Load()),
                                                        attr='res_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='attachment', ctx=Load()),
                                                    attr='res_name',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='display_name',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='attachment', ctx=Load()),
                                                    attr='res_name',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=False, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
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
                    name='_storage',
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
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.config_parameter', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='get_param',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='ir_attachment.location', kind=None),
                                    Constant(value='file', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_filestore',
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
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='config', ctx=Load()),
                                    attr='filestore',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_cr',
                                            ctx=Load(),
                                        ),
                                        attr='dbname',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_storage_domain',
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
                        Return(
                            value=Subscript(
                                value=Dict(
                                    keys=[
                                        Constant(value='db', kind=None),
                                        Constant(value='file', kind=None),
                                    ],
                                    values=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='store_fname', kind=None),
                                                        Constant(value='!=', kind=None),
                                                        Constant(value=False, kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='db_datas', kind=None),
                                                        Constant(value='!=', kind=None),
                                                        Constant(value=False, kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                ),
                                slice=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_storage',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='force_storage',
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
                            value=Constant(value='Force all attachments to be stored in the currently configured storage', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='is_admin',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='AccessError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Only administrators can execute this action.', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='expression', ctx=Load()),
                                                    attr='AND',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_get_storage_domain',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Constant(value='&', kind=None),
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='type', kind=None),
                                                                            Constant(value='=', kind=None),
                                                                            Constant(value='binary', kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value='|', kind=None),
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='res_field', kind=None),
                                                                            Constant(value='=', kind=None),
                                                                            Constant(value=False, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='res_field', kind=None),
                                                                            Constant(value='!=', kind=None),
                                                                            Constant(value=False, kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_migrate',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_migrate',
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
                            targets=[Name(id='record_count', ctx=Store())],
                            value=Call(
                                func=Name(id='len', ctx=Load()),
                                args=[Name(id='self', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='storage', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_storage',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='upper',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='index', ctx=Store()),
                                    Name(id='attach', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='enumerate', ctx=Load()),
                                args=[Name(id='self', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='debug',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='Migrate attachment %s/%s to %s', kind=None),
                                            BinOp(
                                                left=Name(id='index', ctx=Load()),
                                                op=Add(),
                                                right=Constant(value=1, kind=None),
                                            ),
                                            Name(id='record_count', ctx=Load()),
                                            Name(id='storage', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='attach', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='raw', kind=None),
                                                    Constant(value='mimetype', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='attach', ctx=Load()),
                                                        attr='raw',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='attach', ctx=Load()),
                                                        attr='mimetype',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
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
                    name='_full_path',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='path', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='path', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='sub',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='[.]', kind=None),
                                    Constant(value='', kind=None),
                                    Name(id='path', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='path', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='path', ctx=Load()),
                                    attr='strip',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='/\\', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='os', ctx=Load()),
                                        attr='path',
                                        ctx=Load(),
                                    ),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_filestore',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Name(id='path', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_path',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='bin_data', annotation=None, type_comment=None),
                            arg(arg='sha', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='fname', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Subscript(
                                        value=Name(id='sha', ctx=Load()),
                                        slice=Slice(
                                            lower=None,
                                            upper=Constant(value=3, kind=None),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    op=Add(),
                                    right=Constant(value='/', kind=None),
                                ),
                                op=Add(),
                                right=Name(id='sha', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='full_path', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_full_path',
                                    ctx=Load(),
                                ),
                                args=[Name(id='fname', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='os', ctx=Load()),
                                        attr='path',
                                        ctx=Load(),
                                    ),
                                    attr='isfile',
                                    ctx=Load(),
                                ),
                                args=[Name(id='full_path', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=Tuple(
                                        elts=[
                                            Name(id='fname', ctx=Load()),
                                            Name(id='full_path', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='fname', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Subscript(
                                        value=Name(id='sha', ctx=Load()),
                                        slice=Slice(
                                            lower=None,
                                            upper=Constant(value=2, kind=None),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    op=Add(),
                                    right=Constant(value='/', kind=None),
                                ),
                                op=Add(),
                                right=Name(id='sha', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='full_path', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_full_path',
                                    ctx=Load(),
                                ),
                                args=[Name(id='fname', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='dirname', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='os', ctx=Load()),
                                        attr='path',
                                        ctx=Load(),
                                    ),
                                    attr='dirname',
                                    ctx=Load(),
                                ),
                                args=[Name(id='full_path', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='path',
                                            ctx=Load(),
                                        ),
                                        attr='isdir',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='dirname', ctx=Load())],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='makedirs',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='dirname', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            attr='isfile',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='full_path', ctx=Load())],
                                        keywords=[],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_same_content',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Name(id='bin_data', ctx=Load()),
                                                Name(id='full_path', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[Constant(value='The attachment is colliding with an existing file.', kind=None)],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='fname', ctx=Load()),
                                    Name(id='full_path', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_file_read',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='fname', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='full_path', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_full_path',
                                    ctx=Load(),
                                ),
                                args=[Name(id='fname', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Name(id='open', ctx=Load()),
                                                args=[
                                                    Name(id='full_path', ctx=Load()),
                                                    Constant(value='rb', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='f', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='f', ctx=Load()),
                                                    attr='read',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Tuple(
                                        elts=[
                                            Name(id='IOError', ctx=Load()),
                                            Name(id='OSError', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    name=None,
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='info',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='_read_file reading %s', kind=None),
                                                    Name(id='full_path', ctx=Load()),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='exc_info',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Return(
                            value=Constant(value=b'', kind=None),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_file_write',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='bin_value', annotation=None, type_comment=None),
                            arg(arg='checksum', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='fname', ctx=Store()),
                                        Name(id='full_path', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_path',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='bin_value', ctx=Load()),
                                    Name(id='checksum', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='path',
                                            ctx=Load(),
                                        ),
                                        attr='exists',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='full_path', ctx=Load())],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Try(
                                    body=[
                                        With(
                                            items=[
                                                withitem(
                                                    context_expr=Call(
                                                        func=Name(id='open', ctx=Load()),
                                                        args=[
                                                            Name(id='full_path', ctx=Load()),
                                                            Constant(value='wb', kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    optional_vars=Name(id='fp', ctx=Store()),
                                                ),
                                            ],
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='fp', ctx=Load()),
                                                            attr='write',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='bin_value', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_mark_for_gc',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='fname', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='IOError', ctx=Load()),
                                            name=None,
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='info',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='_file_write writing %s', kind=None),
                                                            Name(id='full_path', ctx=Load()),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='exc_info',
                                                                value=Constant(value=True, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='fname', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_file_delete',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='fname', annotation=None, type_comment=None),
                        ],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='_mark_for_gc',
                                    ctx=Load(),
                                ),
                                args=[Name(id='fname', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_mark_for_gc',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='fname', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Add ``fname`` in a checklist for the filestore garbage collection. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='full_path', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='os', ctx=Load()),
                                        attr='path',
                                        ctx=Load(),
                                    ),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_full_path',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='checklist', kind=None)],
                                        keywords=[],
                                    ),
                                    Name(id='fname', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='path',
                                            ctx=Load(),
                                        ),
                                        attr='exists',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='full_path', ctx=Load())],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='dirname', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            attr='dirname',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='full_path', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='os', ctx=Load()),
                                                    attr='path',
                                                    ctx=Load(),
                                                ),
                                                attr='isdir',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='dirname', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        With(
                                            items=[
                                                withitem(
                                                    context_expr=Call(
                                                        func=Attribute(
                                                            value=Name(id='tools', ctx=Load()),
                                                            attr='ignore',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='OSError', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    optional_vars=None,
                                                ),
                                            ],
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='os', ctx=Load()),
                                                            attr='makedirs',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='dirname', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='open', ctx=Load()),
                                                args=[
                                                    Name(id='full_path', ctx=Load()),
                                                    Constant(value='ab', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='close',
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_gc_file_store',
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
                            value=Constant(value=' Perform the garbage collection of the filestore. ', kind=None),
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_storage',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='file', kind=None)],
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='cr', ctx=Store())],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='_cr',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cr', ctx=Load()),
                                    attr='commit',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cr', ctx=Load()),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[Constant(value="SET LOCAL lock_timeout TO '10s'", kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cr', ctx=Load()),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='LOCK ir_attachment IN SHARE MODE', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='checklist', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='dirpath', ctx=Store()),
                                    Name(id='_', ctx=Store()),
                                    Name(id='filenames', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='os', ctx=Load()),
                                    attr='walk',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_full_path',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='checklist', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='dirname', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            attr='basename',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='dirpath', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='filename', ctx=Store()),
                                    iter=Name(id='filenames', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='fname', ctx=Store())],
                                            value=BinOp(
                                                left=Constant(value='%s/%s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='dirname', ctx=Load()),
                                                        Name(id='filename', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='checklist', ctx=Load()),
                                                    slice=Name(id='fname', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='os', ctx=Load()),
                                                        attr='path',
                                                        ctx=Load(),
                                                    ),
                                                    attr='join',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='dirpath', ctx=Load()),
                                                    Name(id='filename', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='whitelist', ctx=Store())],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='names', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='cr', ctx=Load()),
                                    attr='split_for_in_conditions',
                                    ctx=Load(),
                                ),
                                args=[Name(id='checklist', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='cr', ctx=Load()),
                                            attr='execute',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='SELECT store_fname FROM ir_attachment WHERE store_fname IN %s', kind=None),
                                            List(
                                                elts=[Name(id='names', ctx=Load())],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='whitelist', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            GeneratorExp(
                                                elt=Subscript(
                                                    value=Name(id='row', ctx=Load()),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='row', ctx=Store()),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Name(id='cr', ctx=Load()),
                                                                attr='fetchall',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='removed', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='fname', ctx=Store()),
                                    Name(id='filepath', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='checklist', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='fname', ctx=Load()),
                                        ops=[NotIn()],
                                        comparators=[Name(id='whitelist', ctx=Load())],
                                    ),
                                    body=[
                                        Try(
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='os', ctx=Load()),
                                                            attr='unlink',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_full_path',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='fname', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                AugAssign(
                                                    target=Name(id='removed', ctx=Store()),
                                                    op=Add(),
                                                    value=Constant(value=1, kind=None),
                                                ),
                                            ],
                                            handlers=[
                                                ExceptHandler(
                                                    type=Tuple(
                                                        elts=[
                                                            Name(id='OSError', ctx=Load()),
                                                            Name(id='IOError', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    name=None,
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='_logger', ctx=Load()),
                                                                    attr='info',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='_file_gc could not unlink %s', kind=None),
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='_full_path',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='fname', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='exc_info',
                                                                        value=Constant(value=True, kind=None),
                                                                    ),
                                                                ],
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[],
                                            finalbody=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Name(id='tools', ctx=Load()),
                                                    attr='ignore',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='OSError', ctx=Load())],
                                                keywords=[],
                                            ),
                                            optional_vars=None,
                                        ),
                                    ],
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='os', ctx=Load()),
                                                    attr='unlink',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='filepath', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cr', ctx=Load()),
                                    attr='commit',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='filestore gc %d checked, %d removed', kind=None),
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='checklist', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Name(id='removed', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='autovacuum',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_datas',
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
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_context',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='bin_size', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                For(
                                    target=Name(id='attach', ctx=Store()),
                                    iter=Name(id='self', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='attach', ctx=Load()),
                                                    attr='datas',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Name(id='human_size', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='attach', ctx=Load()),
                                                        attr='file_size',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Return(value=None),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Name(id='attach', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='attach', ctx=Load()),
                                            attr='datas',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='base64', ctx=Load()),
                                            attr='b64encode',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Name(id='attach', ctx=Load()),
                                                        attr='raw',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=b'', kind=None),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='store_fname', kind=None),
                                Constant(value='db_datas', kind=None),
                                Constant(value='file_size', kind=None),
                            ],
                            keywords=[],
                        ),
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends_context',
                                ctx=Load(),
                            ),
                            args=[Constant(value='bin_size', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_raw',
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
                        For(
                            target=Name(id='attach', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Name(id='attach', ctx=Load()),
                                        attr='store_fname',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='attach', ctx=Load()),
                                                    attr='raw',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='attach', ctx=Load()),
                                                    attr='_file_read',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='attach', ctx=Load()),
                                                        attr='store_fname',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='attach', ctx=Load()),
                                                    attr='raw',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Name(id='attach', ctx=Load()),
                                                attr='db_datas',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='store_fname', kind=None),
                                Constant(value='db_datas', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_inverse_raw',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='_set_attachment_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='a', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=BoolOp(
                                            op=Or(),
                                            values=[
                                                Attribute(
                                                    value=Name(id='a', ctx=Load()),
                                                    attr='raw',
                                                    ctx=Load(),
                                                ),
                                                Constant(value=b'', kind=None),
                                            ],
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
                    name='_inverse_datas',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='_set_attachment_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='attach', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Call(
                                            func=Attribute(
                                                value=Name(id='base64', ctx=Load()),
                                                attr='b64decode',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        Attribute(
                                                            value=Name(id='attach', ctx=Load()),
                                                            attr='datas',
                                                            ctx=Load(),
                                                        ),
                                                        Constant(value=b'', kind=None),
                                                    ],
                                                ),
                                            ],
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
                    name='_set_attachment_data',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='asbytes', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            target=Name(id='attach', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='bin_data', ctx=Store())],
                                    value=Call(
                                        func=Name(id='asbytes', ctx=Load()),
                                        args=[Name(id='attach', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='vals', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_datas_related_values',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='bin_data', ctx=Load()),
                                            Attribute(
                                                value=Name(id='attach', ctx=Load()),
                                                attr='mimetype',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='fname', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='attach', ctx=Load()),
                                        attr='store_fname',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[
                                                    Name(id='IrAttachment', ctx=Load()),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='attach', ctx=Load()),
                                                            attr='sudo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='vals', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Name(id='fname', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_file_delete',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='fname', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
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
                    name='_get_datas_related_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                            arg(arg='mimetype', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='file_size', kind=None),
                                    Constant(value='checksum', kind=None),
                                    Constant(value='index_content', kind=None),
                                    Constant(value='store_fname', kind=None),
                                    Constant(value='db_datas', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='data', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_compute_checksum',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='data', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_index',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='data', ctx=Load()),
                                            Name(id='mimetype', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=False, kind=None),
                                    Name(id='data', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='data', ctx=Load()),
                                    Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_storage',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='db', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='store_fname', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_file_write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='data', ctx=Load()),
                                            Subscript(
                                                value=Name(id='values', ctx=Load()),
                                                slice=Constant(value='checksum', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='db_datas', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='values', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_checksum',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='bin_data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' compute the checksum for the given datas\n            :param bin_data : datas in its binary form\n        ', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='hashlib', ctx=Load()),
                                            attr='sha1',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Name(id='bin_data', ctx=Load()),
                                                    Constant(value=b'', kind=None),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='hexdigest',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_same_content',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='bin_data', annotation=None, type_comment=None),
                            arg(arg='filepath', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='BLOCK_SIZE', ctx=Store())],
                            value=Constant(value=1024, kind=None),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='open', ctx=Load()),
                                        args=[
                                            Name(id='filepath', ctx=Load()),
                                            Constant(value='rb', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='fd', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='i', ctx=Store())],
                                    value=Constant(value=0, kind=None),
                                    type_comment=None,
                                ),
                                While(
                                    test=Constant(value=True, kind=None),
                                    body=[
                                        Assign(
                                            targets=[Name(id='data', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='fd', ctx=Load()),
                                                    attr='read',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='BLOCK_SIZE', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='data', ctx=Load()),
                                                ops=[NotEq()],
                                                comparators=[
                                                    Subscript(
                                                        value=Name(id='bin_data', ctx=Load()),
                                                        slice=Slice(
                                                            lower=BinOp(
                                                                left=Name(id='i', ctx=Load()),
                                                                op=Mult(),
                                                                right=Name(id='BLOCK_SIZE', ctx=Load()),
                                                            ),
                                                            upper=BinOp(
                                                                left=BinOp(
                                                                    left=Name(id='i', ctx=Load()),
                                                                    op=Add(),
                                                                    right=Constant(value=1, kind=None),
                                                                ),
                                                                op=Mult(),
                                                                right=Name(id='BLOCK_SIZE', ctx=Load()),
                                                            ),
                                                            step=None,
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Return(
                                                    value=Constant(value=False, kind=None),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Name(id='data', ctx=Load()),
                                            ),
                                            body=[Break()],
                                            orelse=[],
                                        ),
                                        AugAssign(
                                            target=Name(id='i', ctx=Store()),
                                            op=Add(),
                                            value=Constant(value=1, kind=None),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            type_comment=None,
                        ),
                        Return(
                            value=Constant(value=True, kind=None),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_mimetype',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' compute the mimetype of the given values\n            :param values : dict of values to create or write an ir_attachment\n            :return mime : string indicating the mimetype, or application/octet-stream by default\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='mimetype', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='values', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='mimetype', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='mimetype', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='values', ctx=Load()),
                                        slice=Constant(value='mimetype', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='mimetype', ctx=Load()),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='name', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='mimetype', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='mimetypes', ctx=Load()),
                                                attr='guess_type',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Constant(value='name', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='mimetype', ctx=Load()),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='url', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='mimetype', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='mimetypes', ctx=Load()),
                                                attr='guess_type',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Subscript(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='values', ctx=Load()),
                                                                slice=Constant(value='url', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='split',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='?', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='mimetype', ctx=Load()),
                                    ),
                                    Compare(
                                        left=Name(id='mimetype', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='application/octet-stream', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='raw', ctx=Store())],
                                    value=Constant(value=None, kind=None),
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='raw', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='raw', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='values', ctx=Load()),
                                                slice=Constant(value='raw', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Call(
                                                func=Attribute(
                                                    value=Name(id='values', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='datas', kind=None)],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='raw', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='base64', ctx=Load()),
                                                            attr='b64decode',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='values', ctx=Load()),
                                                                slice=Constant(value='datas', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                                If(
                                    test=Name(id='raw', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='mimetype', ctx=Store())],
                                            value=Call(
                                                func=Name(id='guess_mimetype', ctx=Load()),
                                                args=[Name(id='raw', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='mimetype', ctx=Load()),
                                    Constant(value='application/octet-stream', kind=None),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_postprocess_contents',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='ICP', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='ir.config_parameter', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='sudo',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                attr='get_param',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='supported_subtype', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='ICP', ctx=Load()),
                                        args=[
                                            Constant(value='base.image_autoresize_extensions', kind=None),
                                            Constant(value='png,jpeg,gif,bmp,tif', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='split',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=',', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Name(id='mimetype', ctx=Store()),
                                Subscript(
                                    value=Name(id='values', ctx=Load()),
                                    slice=Constant(value='mimetype', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_compute_mimetype',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='_type', ctx=Store()),
                                        Name(id='_subtype', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='mimetype', ctx=Load()),
                                    attr='split',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='/', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='is_image_resizable', ctx=Store())],
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Name(id='_type', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='image', kind=None)],
                                    ),
                                    Compare(
                                        left=Name(id='_subtype', ctx=Load()),
                                        ops=[In()],
                                        comparators=[Name(id='supported_subtype', ctx=Load())],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='is_image_resizable', ctx=Load()),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='values', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='datas', kind=None)],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='values', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='raw', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='is_raw', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='raw', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='max_resolution', ctx=Store())],
                                    value=Call(
                                        func=Name(id='ICP', ctx=Load()),
                                        args=[
                                            Constant(value='base.image_autoresize_max_px', kind=None),
                                            Constant(value='1920x1920', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Name(id='str2bool', ctx=Load()),
                                        args=[
                                            Name(id='max_resolution', ctx=Load()),
                                            Constant(value=True, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Try(
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Name(id='img', ctx=Store()),
                                                        Name(id='fn_quality', ctx=Store()),
                                                    ],
                                                    value=Constant(value=False, kind=None),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Name(id='is_raw', ctx=Load()),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='img', ctx=Store())],
                                                            value=Call(
                                                                func=Name(id='ImageProcess', ctx=Load()),
                                                                args=[Constant(value=False, kind=None)],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='verify_resolution',
                                                                        value=Constant(value=False, kind=None),
                                                                    ),
                                                                ],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='img', ctx=Load()),
                                                                    attr='image',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='Image', ctx=Load()),
                                                                    attr='open',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='io', ctx=Load()),
                                                                            attr='BytesIO',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Subscript(
                                                                                value=Name(id='values', ctx=Load()),
                                                                                slice=Constant(value='raw', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='img', ctx=Load()),
                                                                    attr='original_format',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=BoolOp(
                                                                        op=Or(),
                                                                        values=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='img', ctx=Load()),
                                                                                    attr='image',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='format',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value='', kind=None),
                                                                        ],
                                                                    ),
                                                                    attr='upper',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='fn_quality', ctx=Store())],
                                                            value=Attribute(
                                                                value=Name(id='img', ctx=Load()),
                                                                attr='image_quality',
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Assign(
                                                            targets=[Name(id='img', ctx=Store())],
                                                            value=Call(
                                                                func=Name(id='ImageProcess', ctx=Load()),
                                                                args=[
                                                                    Subscript(
                                                                        value=Name(id='values', ctx=Load()),
                                                                        slice=Constant(value='datas', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='verify_resolution',
                                                                        value=Constant(value=False, kind=None),
                                                                    ),
                                                                ],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='fn_quality', ctx=Store())],
                                                            value=Attribute(
                                                                value=Name(id='img', ctx=Load()),
                                                                attr='image_base64',
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                ),
                                                Assign(
                                                    targets=[
                                                        Tuple(
                                                            elts=[
                                                                Name(id='w', ctx=Store()),
                                                                Name(id='h', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='img', ctx=Load()),
                                                            attr='image',
                                                            ctx=Load(),
                                                        ),
                                                        attr='size',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Tuple(
                                                            elts=[
                                                                Name(id='nw', ctx=Store()),
                                                                Name(id='nh', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Name(id='map', ctx=Load()),
                                                        args=[
                                                            Name(id='int', ctx=Load()),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='max_resolution', ctx=Load()),
                                                                    attr='split',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='x', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Compare(
                                                                left=Name(id='w', ctx=Load()),
                                                                ops=[Gt()],
                                                                comparators=[Name(id='nw', ctx=Load())],
                                                            ),
                                                            Compare(
                                                                left=Name(id='h', ctx=Load()),
                                                                ops=[Gt()],
                                                                comparators=[Name(id='nh', ctx=Load())],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='img', ctx=Load()),
                                                                    attr='resize',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='nw', ctx=Load()),
                                                                    Name(id='nh', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='quality', ctx=Store())],
                                                            value=Call(
                                                                func=Name(id='int', ctx=Load()),
                                                                args=[
                                                                    Call(
                                                                        func=Name(id='ICP', ctx=Load()),
                                                                        args=[
                                                                            Constant(value='base.image_autoresize_quality', kind=None),
                                                                            Constant(value=80, kind=None),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='values', ctx=Load()),
                                                                    slice=BoolOp(
                                                                        op=Or(),
                                                                        values=[
                                                                            BoolOp(
                                                                                op=And(),
                                                                                values=[
                                                                                    Name(id='is_raw', ctx=Load()),
                                                                                    Constant(value='raw', kind=None),
                                                                                ],
                                                                            ),
                                                                            Constant(value='datas', kind=None),
                                                                        ],
                                                                    ),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Call(
                                                                func=Name(id='fn_quality', ctx=Load()),
                                                                args=[],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='quality',
                                                                        value=Name(id='quality', ctx=Load()),
                                                                    ),
                                                                ],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            handlers=[
                                                ExceptHandler(
                                                    type=Name(id='UserError', ctx=Load()),
                                                    name='e',
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='_logger', ctx=Load()),
                                                                    attr='info',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='Post processing ignored : %s', kind=None),
                                                                    Name(id='e', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Pass(),
                                                    ],
                                                ),
                                            ],
                                            orelse=[],
                                            finalbody=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='values', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_contents',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Name(id='mimetype', ctx=Store()),
                                Subscript(
                                    value=Name(id='values', ctx=Load()),
                                    slice=Constant(value='mimetype', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_compute_mimetype',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='xml_like', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Compare(
                                        left=Constant(value='ht', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='mimetype', ctx=Load())],
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Constant(value='xml', kind=None),
                                                ops=[In()],
                                                comparators=[Name(id='mimetype', ctx=Load())],
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Compare(
                                                    left=Constant(value='openxmlformats', kind=None),
                                                    ops=[In()],
                                                    comparators=[Name(id='mimetype', ctx=Load())],
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='user', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='binary_field_real_user', kind=None),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='user',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='force_text', ctx=Store())],
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='xml_like', ctx=Load()),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Name(id='user', ctx=Load()),
                                                        attr='_is_system',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='context',
                                                        ctx=Load(),
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='attachments_mime_plainxml', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='force_text', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='mimetype', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='text/plain', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='context',
                                            ctx=Load(),
                                        ),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='image_no_postprocess', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='values', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_postprocess_contents',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='values', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='values', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_index',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='bin_data', annotation=None, type_comment=None),
                            arg(arg='file_type', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" compute the index content of the given binary data.\n            This is a python implementation of the unix command 'strings'.\n            :param bin_data : datas in binary form\n            :return index_content : string containing all the printable character of the binary data\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='index_content', ctx=Store())],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='file_type', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='index_content', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='file_type', ctx=Load()),
                                                attr='split',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='/', kind=None)],
                                            keywords=[],
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='index_content', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='text', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='words', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='re', ctx=Load()),
                                                    attr='findall',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value=b'[ -~]{4,}', kind=None),
                                                    Name(id='bin_data', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='index_content', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Constant(value=b'\n', kind=None),
                                                            attr='join',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='words', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    attr='decode',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='ascii', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='index_content', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_serving_groups',
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
                            value=Constant(value=' An ir.attachment record may be used as a fallback in the\n        http dispatch if its type field is set to "binary" and its url\n        field is set as the request\'s url. Only the groups returned by\n        this method are allowed to create and write on such records.\n        ', kind=None),
                        ),
                        Return(
                            value=List(
                                elts=[Constant(value='base.group_system', kind=None)],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Name', kind=None)],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='description', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Text',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Description', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='res_name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Resource Name', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_res_name', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='res_model', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Resource Model', kind=None)],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The database object this attachment will be attached to.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='res_field', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Resource Field', kind=None)],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='res_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2oneReference',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Resource ID', kind=None)],
                        keywords=[
                            keyword(
                                arg='model_field',
                                value=Constant(value='res_model', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The record id this is attached to.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='company_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.company', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Company', kind=None),
                            ),
                            keyword(
                                arg='change_default',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='company',
                                        ctx=Load(),
                                    ),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='type', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='url', kind=None),
                                            Constant(value='URL', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='binary', kind=None),
                                            Constant(value='File', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Type', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='binary', kind=None),
                            ),
                            keyword(
                                arg='change_default',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='You can either upload a file from your computer or copy/paste an internet link to your file.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='url', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Url', kind=None)],
                        keywords=[
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='size',
                                value=Constant(value=1024, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='public', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Is public document', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='access_token', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Access Token', kind=None)],
                        keywords=[
                            keyword(
                                arg='groups',
                                value=Constant(value='base.group_user', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='raw', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Binary',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='File Content (raw)', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_raw', kind=None),
                            ),
                            keyword(
                                arg='inverse',
                                value=Constant(value='_inverse_raw', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='datas', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Binary',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='File Content (base64)', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_datas', kind=None),
                            ),
                            keyword(
                                arg='inverse',
                                value=Constant(value='_inverse_datas', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='db_datas', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Binary',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Database Data', kind=None)],
                        keywords=[
                            keyword(
                                arg='attachment',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='store_fname', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Stored Filename', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='file_size', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(value='File Size', kind=None)],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='checksum', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Checksum/SHA1', kind=None)],
                        keywords=[
                            keyword(
                                arg='size',
                                value=Constant(value=40, kind=None),
                            ),
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='mimetype', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Mime Type', kind=None)],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='index_content', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Text',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Indexed Content', kind=None)],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='prefetch',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_auto_init',
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
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='IrAttachment', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_auto_init',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='create_index',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_cr',
                                        ctx=Load(),
                                    ),
                                    Constant(value='ir_attachment_res_idx', kind=None),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_table',
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='res_model', kind=None),
                                            Constant(value='res_id', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_serving_attachments',
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
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='is_admin',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        For(
                            target=Name(id='attachment', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='attachment', ctx=Load()),
                                                    attr='type',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='binary', kind=None)],
                                            ),
                                            Attribute(
                                                value=Name(id='attachment', ctx=Load()),
                                                attr='url',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='has_group', ctx=Store())],
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='user',
                                                    ctx=Load(),
                                                ),
                                                attr='has_group',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Name(id='any', ctx=Load()),
                                                    args=[
                                                        GeneratorExp(
                                                            elt=Call(
                                                                func=Name(id='has_group', ctx=Load()),
                                                                args=[Name(id='g', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            generators=[
                                                                comprehension(
                                                                    target=Name(id='g', ctx=Store()),
                                                                    iter=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='attachment', ctx=Load()),
                                                                            attr='get_serving_groups',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                    ifs=[],
                                                                    is_async=0,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='ValidationError', ctx=Load()),
                                                        args=[Constant(value='Sorry, you are not allowed to write on this document', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    cause=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='constrains',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='type', kind=None),
                                Constant(value='url', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='check',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='mode', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Restricts the access to an ir.attachment, according to referred mode ', kind=None),
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='is_superuser',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=BoolOp(
                                    op=Or(),
                                    values=[
                                        Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='is_admin',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='user',
                                                    ctx=Load(),
                                                ),
                                                attr='has_group',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='base.group_user', kind=None)],
                                            keywords=[],
                                        ),
                                    ],
                                ),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='AccessError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Sorry, you are not allowed to access this document.', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='model_ids', ctx=Store())],
                            value=Call(
                                func=Name(id='defaultdict', ctx=Load()),
                                args=[Name(id='set', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='self', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.attachment', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='flush',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Constant(value='res_model', kind=None),
                                                    Constant(value='res_id', kind=None),
                                                    Constant(value='create_uid', kind=None),
                                                    Constant(value='public', kind=None),
                                                    Constant(value='res_field', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_cr',
                                                ctx=Load(),
                                            ),
                                            attr='execute',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='SELECT res_model, res_id, create_uid, public, res_field FROM ir_attachment WHERE id IN %s', kind=None),
                                            List(
                                                elts=[
                                                    Call(
                                                        func=Name(id='tuple', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='ids',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='res_model', ctx=Store()),
                                            Name(id='res_id', ctx=Store()),
                                            Name(id='create_uid', ctx=Store()),
                                            Name(id='public', ctx=Store()),
                                            Name(id='res_field', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_cr',
                                                ctx=Load(),
                                            ),
                                            attr='fetchall',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='is_system',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    Name(id='res_field', ctx=Load()),
                                                ],
                                            ),
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='AccessError', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='Sorry, you are not allowed to access this document.', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    cause=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='public', ctx=Load()),
                                                    Compare(
                                                        left=Name(id='mode', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='read', kind=None)],
                                                    ),
                                                ],
                                            ),
                                            body=[Continue()],
                                            orelse=[],
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=BoolOp(
                                                    op=And(),
                                                    values=[
                                                        Name(id='res_model', ctx=Load()),
                                                        Name(id='res_id', ctx=Load()),
                                                    ],
                                                ),
                                            ),
                                            body=[Continue()],
                                            orelse=[],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='model_ids', ctx=Load()),
                                                        slice=Name(id='res_model', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    attr='add',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='res_id', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='values', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='res_model', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='res_id', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='model_ids', ctx=Load()),
                                                slice=Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Constant(value='res_model', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            attr='add',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='values', ctx=Load()),
                                                slice=Constant(value='res_id', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='res_model', ctx=Store()),
                                    Name(id='res_ids', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='model_ids', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='res_model', ctx=Load()),
                                        ops=[NotIn()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='res_model', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='res.users', kind=None)],
                                            ),
                                            Compare(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[Name(id='res_ids', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value=1, kind=None)],
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='uid',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[
                                                    Subscript(
                                                        value=Call(
                                                            func=Name(id='list', ctx=Load()),
                                                            args=[Name(id='res_ids', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='records', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Name(id='res_model', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='res_ids', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='exists',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='access_mode', ctx=Store())],
                                    value=IfExp(
                                        test=Compare(
                                            left=Name(id='mode', ctx=Load()),
                                            ops=[In()],
                                            comparators=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='create', kind=None),
                                                        Constant(value='unlink', kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                        body=Constant(value='write', kind=None),
                                        orelse=Name(id='mode', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='records', ctx=Load()),
                                            attr='check_access_rights',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='access_mode', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='records', ctx=Load()),
                                            attr='check_access_rule',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='access_mode', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_read_group_allowed_fields',
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
                        Return(
                            value=List(
                                elts=[
                                    Constant(value='type', kind=None),
                                    Constant(value='company_id', kind=None),
                                    Constant(value='res_id', kind=None),
                                    Constant(value='create_date', kind=None),
                                    Constant(value='create_uid', kind=None),
                                    Constant(value='name', kind=None),
                                    Constant(value='mimetype', kind=None),
                                    Constant(value='id', kind=None),
                                    Constant(value='url', kind=None),
                                    Constant(value='res_field', kind=None),
                                    Constant(value='res_model', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='read_group',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='domain', annotation=None, type_comment=None),
                            arg(arg='fields', annotation=None, type_comment=None),
                            arg(arg='groupby', annotation=None, type_comment=None),
                            arg(arg='offset', annotation=None, type_comment=None),
                            arg(arg='limit', annotation=None, type_comment=None),
                            arg(arg='orderby', annotation=None, type_comment=None),
                            arg(arg='lazy', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=0, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=True, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Override read_group to add res_field=False in domain if not present.', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='fields', ctx=Load()),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='AccessError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Sorry, you must provide fields to read on attachments', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='groupby', ctx=Store())],
                            value=IfExp(
                                test=Call(
                                    func=Name(id='isinstance', ctx=Load()),
                                    args=[
                                        Name(id='groupby', ctx=Load()),
                                        Name(id='str', ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                                body=List(
                                    elts=[Name(id='groupby', ctx=Load())],
                                    ctx=Load(),
                                ),
                                orelse=Name(id='groupby', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Name(id='any', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Compare(
                                            left=Constant(value='(', kind=None),
                                            ops=[In()],
                                            comparators=[Name(id='field', ctx=Load())],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='field', ctx=Store()),
                                                iter=BinOp(
                                                    left=Name(id='fields', ctx=Load()),
                                                    op=Add(),
                                                    right=Name(id='groupby', ctx=Load()),
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='AccessError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value="Sorry, the syntax 'name:agg(field)' is not available for attachments", kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Name(id='any', ctx=Load()),
                                    args=[
                                        GeneratorExp(
                                            elt=Compare(
                                                left=Subscript(
                                                    value=Name(id='item', ctx=Load()),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[In()],
                                                comparators=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='id', kind=None),
                                                            Constant(value='res_field', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            generators=[
                                                comprehension(
                                                    target=Name(id='item', ctx=Store()),
                                                    iter=Name(id='domain', ctx=Load()),
                                                    ifs=[],
                                                    is_async=0,
                                                ),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='domain', ctx=Load()),
                                            attr='insert',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=0, kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value='res_field', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='allowed_fields', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_read_group_allowed_fields',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='fields_set', ctx=Store())],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Subscript(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='field', ctx=Load()),
                                                    attr='split',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value=':', kind=None)],
                                                keywords=[],
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='field', ctx=Store()),
                                                iter=BinOp(
                                                    left=Name(id='fields', ctx=Load()),
                                                    op=Add(),
                                                    right=Name(id='groupby', ctx=Load()),
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='is_system',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='fields', ctx=Load()),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='fields_set', ctx=Load()),
                                                    attr='difference',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='allowed_fields', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='AccessError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Sorry, you are not allowed to access these fields on attachments.', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='domain', ctx=Load()),
                                    Name(id='fields', ctx=Load()),
                                    Name(id='groupby', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='offset',
                                        value=Name(id='offset', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='limit',
                                        value=Name(id='limit', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='orderby',
                                        value=Name(id='orderby', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='lazy',
                                        value=Name(id='lazy', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_search',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='args', annotation=None, type_comment=None),
                            arg(arg='offset', annotation=None, type_comment=None),
                            arg(arg='limit', annotation=None, type_comment=None),
                            arg(arg='order', annotation=None, type_comment=None),
                            arg(arg='count', annotation=None, type_comment=None),
                            arg(arg='access_rights_uid', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=0, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='discard_binary_fields_attachments', ctx=Store())],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Name(id='any', ctx=Load()),
                                    args=[
                                        GeneratorExp(
                                            elt=Compare(
                                                left=Subscript(
                                                    value=Name(id='arg', ctx=Load()),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[In()],
                                                comparators=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='id', kind=None),
                                                            Constant(value='res_field', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            generators=[
                                                comprehension(
                                                    target=Name(id='arg', ctx=Store()),
                                                    iter=Name(id='args', ctx=Load()),
                                                    ifs=[],
                                                    is_async=0,
                                                ),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='discard_binary_fields_attachments', ctx=Store())],
                                    value=Constant(value=True, kind=None),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='args', ctx=Load()),
                                            attr='insert',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=0, kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value='res_field', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='ids', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='IrAttachment', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_search',
                                    ctx=Load(),
                                ),
                                args=[Name(id='args', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='offset',
                                        value=Name(id='offset', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='limit',
                                        value=Name(id='limit', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='order',
                                        value=Name(id='order', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='count',
                                        value=Constant(value=False, kind=None),
                                    ),
                                    keyword(
                                        arg='access_rights_uid',
                                        value=Name(id='access_rights_uid', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='is_superuser',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=IfExp(
                                        test=Name(id='count', ctx=Load()),
                                        body=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='ids', ctx=Load())],
                                            keywords=[],
                                        ),
                                        orelse=Name(id='ids', ctx=Load()),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='ids', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=IfExp(
                                        test=Name(id='count', ctx=Load()),
                                        body=Constant(value=0, kind=None),
                                        orelse=List(elts=[], ctx=Load()),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='orig_ids', ctx=Store())],
                            value=Name(id='ids', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ids', ctx=Store())],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[Name(id='ids', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='model_attachments', ctx=Store())],
                            value=Call(
                                func=Name(id='defaultdict', ctx=Load()),
                                args=[
                                    Lambda(
                                        args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                                        body=Call(
                                            func=Name(id='defaultdict', ctx=Load()),
                                            args=[Name(id='set', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='binary_fields_attachments', ctx=Store())],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='SELECT id, res_model, res_id, public, res_field FROM ir_attachment WHERE id IN %s', kind=None),
                                    List(
                                        elts=[
                                            Call(
                                                func=Name(id='tuple', ctx=Load()),
                                                args=[Name(id='ids', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='row', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_cr',
                                        ctx=Load(),
                                    ),
                                    attr='dictfetchall',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Subscript(
                                                    value=Name(id='row', ctx=Load()),
                                                    slice=Constant(value='res_model', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Subscript(
                                                value=Name(id='row', ctx=Load()),
                                                slice=Constant(value='public', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Subscript(
                                                    value=Name(id='model_attachments', ctx=Load()),
                                                    slice=Subscript(
                                                        value=Name(id='row', ctx=Load()),
                                                        slice=Constant(value='res_model', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    ctx=Load(),
                                                ),
                                                slice=Subscript(
                                                    value=Name(id='row', ctx=Load()),
                                                    slice=Constant(value='res_id', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            attr='add',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='row', ctx=Load()),
                                                slice=Constant(value='id', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='discard_binary_fields_attachments', ctx=Load()),
                                            Subscript(
                                                value=Name(id='row', ctx=Load()),
                                                slice=Constant(value='res_field', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='binary_fields_attachments', ctx=Load()),
                                                    attr='add',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='row', ctx=Load()),
                                                        slice=Constant(value='id', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='binary_fields_attachments', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='ids', ctx=Load()),
                                            attr='difference_update',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='binary_fields_attachments', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='res_model', ctx=Store()),
                                    Name(id='targets', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='model_attachments', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='res_model', ctx=Load()),
                                        ops=[NotIn()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Name(id='res_model', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                attr='check_access_rights',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Constant(value='read', kind=None),
                                                Constant(value=False, kind=None),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='ids', ctx=Load()),
                                                    attr='difference_update',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='itertools', ctx=Load()),
                                                            attr='chain',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Starred(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='targets', ctx=Load()),
                                                                        attr='values',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Continue(),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='target_ids', ctx=Store())],
                                    value=Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[Name(id='targets', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='allowed', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Name(id='res_model', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='active_test',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                ],
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='id', kind=None),
                                                            Constant(value='in', kind=None),
                                                            Name(id='target_ids', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='res_id', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='set', ctx=Load()),
                                                args=[Name(id='target_ids', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='difference',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='allowed', ctx=Load()),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='ids', ctx=Load()),
                                                    attr='difference_update',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='targets', ctx=Load()),
                                                        slice=Name(id='res_id', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=ListComp(
                                elt=Name(id='id', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Name(id='id', ctx=Store()),
                                        iter=Name(id='orig_ids', ctx=Load()),
                                        ifs=[
                                            Compare(
                                                left=Name(id='id', ctx=Load()),
                                                ops=[In()],
                                                comparators=[Name(id='ids', ctx=Load())],
                                            ),
                                        ],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='orig_ids', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Name(id='limit', ctx=Load())],
                                    ),
                                    Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='result', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Lt()],
                                        comparators=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_context',
                                                        ctx=Load(),
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='need', kind=None),
                                                    Name(id='limit', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='need', ctx=Store())],
                                    value=BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_context',
                                                    ctx=Load(),
                                                ),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Constant(value='need', kind=None),
                                                Name(id='limit', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                        op=Sub(),
                                        right=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='result', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='extend',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='with_context',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='need',
                                                                    value=Name(id='need', ctx=Load()),
                                                                ),
                                                            ],
                                                        ),
                                                        attr='_search',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='args', ctx=Load())],
                                                    keywords=[
                                                        keyword(
                                                            arg='offset',
                                                            value=BinOp(
                                                                left=Name(id='offset', ctx=Load()),
                                                                op=Add(),
                                                                right=Call(
                                                                    func=Name(id='len', ctx=Load()),
                                                                    args=[Name(id='orig_ids', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                        ),
                                                        keyword(
                                                            arg='limit',
                                                            value=Name(id='limit', ctx=Load()),
                                                        ),
                                                        keyword(
                                                            arg='order',
                                                            value=Name(id='order', ctx=Load()),
                                                        ),
                                                        keyword(
                                                            arg='count',
                                                            value=Name(id='count', ctx=Load()),
                                                        ),
                                                        keyword(
                                                            arg='access_rights_uid',
                                                            value=Name(id='access_rights_uid', ctx=Load()),
                                                        ),
                                                    ],
                                                ),
                                                slice=Slice(
                                                    lower=None,
                                                    upper=BinOp(
                                                        left=Name(id='limit', ctx=Load()),
                                                        op=Sub(),
                                                        right=Call(
                                                            func=Name(id='len', ctx=Load()),
                                                            args=[Name(id='result', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=IfExp(
                                test=Name(id='count', ctx=Load()),
                                body=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='result', ctx=Load())],
                                    keywords=[],
                                ),
                                orelse=Call(
                                    func=Name(id='list', ctx=Load()),
                                    args=[Name(id='result', ctx=Load())],
                                    keywords=[],
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_read',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='fields', annotation=None, type_comment=None),
                        ],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='check',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='read', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='IrAttachment', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_read',
                                    ctx=Load(),
                                ),
                                args=[Name(id='fields', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='write',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals', annotation=None, type_comment=None),
                        ],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='check',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='write', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='values',
                                        value=Name(id='vals', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                        For(
                            target=Name(id='field', ctx=Store()),
                            iter=Tuple(
                                elts=[
                                    Constant(value='file_size', kind=None),
                                    Constant(value='checksum', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='vals', ctx=Load()),
                                            attr='pop',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='field', ctx=Load()),
                                            Constant(value=False, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Compare(
                                        left=Constant(value='mimetype', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='vals', ctx=Load())],
                                    ),
                                    Compare(
                                        left=Constant(value='datas', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='vals', ctx=Load())],
                                    ),
                                    Compare(
                                        left=Constant(value='raw', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='vals', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='vals', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_check_contents',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='vals', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='IrAttachment', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='copy',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='default', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='check',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='write', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='IrAttachment', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='copy',
                                    ctx=Load(),
                                ),
                                args=[Name(id='default', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='unlink',
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
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='self', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='check',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='unlink', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='to_delete', ctx=Store())],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Attribute(
                                            value=Name(id='attach', ctx=Load()),
                                            attr='store_fname',
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='attach', ctx=Store()),
                                                iter=Name(id='self', ctx=Load()),
                                                ifs=[
                                                    Attribute(
                                                        value=Name(id='attach', ctx=Load()),
                                                        attr='store_fname',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='IrAttachment', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='file_path', ctx=Store()),
                            iter=Name(id='to_delete', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_file_delete',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='file_path', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='create',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals_list', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='record_tuple_set', ctx=Store())],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='values', ctx=Store()),
                            iter=Name(id='vals_list', ctx=Load()),
                            body=[
                                For(
                                    target=Name(id='field', ctx=Store()),
                                    iter=Tuple(
                                        elts=[
                                            Constant(value='file_size', kind=None),
                                            Constant(value='checksum', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='values', ctx=Load()),
                                                    attr='pop',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='field', ctx=Load()),
                                                    Constant(value=False, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='values', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_check_contents',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='values', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='raw', ctx=Store()),
                                                Name(id='datas', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Tuple(
                                        elts=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='values', ctx=Load()),
                                                    attr='pop',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='raw', kind=None),
                                                    Constant(value=None, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='values', ctx=Load()),
                                                    attr='pop',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='datas', kind=None),
                                                    Constant(value=None, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='raw', ctx=Load()),
                                            Name(id='datas', ctx=Load()),
                                        ],
                                    ),
                                    body=[
                                        If(
                                            test=Call(
                                                func=Name(id='isinstance', ctx=Load()),
                                                args=[
                                                    Name(id='raw', ctx=Load()),
                                                    Name(id='str', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='raw', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='raw', ctx=Load()),
                                                            attr='encode',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='values', ctx=Load()),
                                                    attr='update',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_get_datas_related_values',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            BoolOp(
                                                                op=Or(),
                                                                values=[
                                                                    Name(id='raw', ctx=Load()),
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='base64', ctx=Load()),
                                                                            attr='b64decode',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            BoolOp(
                                                                                op=Or(),
                                                                                values=[
                                                                                    Name(id='datas', ctx=Load()),
                                                                                    Constant(value=b'', kind=None),
                                                                                ],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                            ),
                                                            Subscript(
                                                                value=Name(id='values', ctx=Load()),
                                                                slice=Constant(value='mimetype', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='record_tuple', ctx=Store())],
                                    value=Tuple(
                                        elts=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='values', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='res_model', kind=None)],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='values', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='res_id', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='record_tuple_set', ctx=Load()),
                                            attr='add',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='record_tuple', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='record_tuple', ctx=Store()),
                            iter=Name(id='record_tuple_set', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='res_model', ctx=Store()),
                                                Name(id='res_id', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='record_tuple', ctx=Load()),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='check',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='create', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='values',
                                                value=Dict(
                                                    keys=[
                                                        Constant(value='res_model', kind=None),
                                                        Constant(value='res_id', kind=None),
                                                    ],
                                                    values=[
                                                        Name(id='res_model', ctx=Load()),
                                                        Name(id='res_id', ctx=Load()),
                                                    ],
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='IrAttachment', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals_list', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model_create_multi',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_post_add_create',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[Pass()],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='generate_access_token',
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
                            targets=[Name(id='tokens', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='attachment', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Name(id='attachment', ctx=Load()),
                                        attr='access_token',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='tokens', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='attachment', ctx=Load()),
                                                        attr='access_token',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Continue(),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='access_token', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_generate_access_token',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='attachment', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='access_token', kind=None)],
                                                values=[Name(id='access_token', ctx=Load())],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tokens', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='access_token', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='tokens', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_generate_access_token',
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
                        Return(
                            value=Call(
                                func=Name(id='str', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='uuid', ctx=Load()),
                                            attr='uuid4',
                                            ctx=Load(),
                                        ),
                                        args=[],
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
                    name='action_get',
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
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.actions.act_window', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_for_xml_id',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='base.action_attachment', kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_serve_attachment',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='url', annotation=None, type_comment=None),
                            arg(arg='extra_domain', annotation=None, type_comment=None),
                            arg(arg='extra_fields', annotation=None, type_comment=None),
                            arg(arg='order', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=BinOp(
                                left=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='type', kind=None),
                                                Constant(value='=', kind=None),
                                                Constant(value='binary', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='url', kind=None),
                                                Constant(value='=', kind=None),
                                                Name(id='url', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=BoolOp(
                                    op=Or(),
                                    values=[
                                        Name(id='extra_domain', ctx=Load()),
                                        List(elts=[], ctx=Load()),
                                    ],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='fieldNames', ctx=Store())],
                            value=BinOp(
                                left=List(
                                    elts=[
                                        Constant(value='__last_update', kind=None),
                                        Constant(value='datas', kind=None),
                                        Constant(value='mimetype', kind=None),
                                    ],
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=BoolOp(
                                    op=Or(),
                                    values=[
                                        Name(id='extra_fields', ctx=Load()),
                                        List(elts=[], ctx=Load()),
                                    ],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='search_read',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='domain', ctx=Load()),
                                    Name(id='fieldNames', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Name(id='order', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='limit',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
