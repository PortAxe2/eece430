USE [master]
GO
/****** Object:  Database [430PROJECT]    Script Date: 5/4/2021 9:03:23 PM ******/
CREATE DATABASE [430PROJECT]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'430PROJECT', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\DATA\430PROJECT.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'430PROJECT_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\DATA\430PROJECT_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT
GO
ALTER DATABASE [430PROJECT] SET COMPATIBILITY_LEVEL = 150
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [430PROJECT].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [430PROJECT] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [430PROJECT] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [430PROJECT] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [430PROJECT] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [430PROJECT] SET ARITHABORT OFF 
GO
ALTER DATABASE [430PROJECT] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [430PROJECT] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [430PROJECT] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [430PROJECT] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [430PROJECT] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [430PROJECT] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [430PROJECT] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [430PROJECT] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [430PROJECT] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [430PROJECT] SET  DISABLE_BROKER 
GO
ALTER DATABASE [430PROJECT] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [430PROJECT] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [430PROJECT] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [430PROJECT] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [430PROJECT] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [430PROJECT] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [430PROJECT] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [430PROJECT] SET RECOVERY SIMPLE 
GO
ALTER DATABASE [430PROJECT] SET  MULTI_USER 
GO
ALTER DATABASE [430PROJECT] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [430PROJECT] SET DB_CHAINING OFF 
GO
ALTER DATABASE [430PROJECT] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [430PROJECT] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [430PROJECT] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [430PROJECT] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
ALTER DATABASE [430PROJECT] SET QUERY_STORE = OFF
GO
USE [430PROJECT]
GO
/****** Object:  Table [dbo].[congratulations]    Script Date: 5/4/2021 9:03:23 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[congratulations](
	[weddingID] [int] NOT NULL,
	[username] [varchar](25) NOT NULL,
	[congratsMessage] [varchar](300) NOT NULL,
	[messageID] [int] IDENTITY(1,1) NOT NULL,
 CONSTRAINT [PK__congratu__33D4145A527D1BD7] PRIMARY KEY CLUSTERED 
(
	[weddingID] ASC,
	[username] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[hasWeddings]    Script Date: 5/4/2021 9:03:23 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[hasWeddings](
	[weddingID] [int] NOT NULL,
	[username] [varchar](25) NOT NULL,
	[ownershipID] [int] IDENTITY(1,1) NOT NULL,
 CONSTRAINT [pkHasID] PRIMARY KEY CLUSTERED 
(
	[weddingID] ASC,
	[username] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[moneyTransfer]    Script Date: 5/4/2021 9:03:23 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[moneyTransfer](
	[weddingID] [int] NOT NULL,
	[username] [varchar](25) NOT NULL,
	[moneyAmount] [real] NULL,
	[transactionID] [int] IDENTITY(1,1) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[weddingID] ASC,
	[username] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[userAttending]    Script Date: 5/4/2021 9:03:23 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[userAttending](
	[username] [varchar](25) NOT NULL,
	[weddingID] [int] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[username] ASC,
	[weddingID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[users]    Script Date: 5/4/2021 9:03:23 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[users](
	[username] [varchar](25) NOT NULL,
	[email] [varchar](25) NOT NULL,
	[FirstName] [varchar](25) NOT NULL,
	[LastName] [varchar](25) NOT NULL,
	[UserPassword] [varchar](25) NOT NULL,
	[isAdmin] [bit] NOT NULL,
 CONSTRAINT [PK__users__F3DBC573572AF875] PRIMARY KEY CLUSTERED 
(
	[username] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[weddings]    Script Date: 5/4/2021 9:03:23 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[weddings](
	[weddingID] [int] IDENTITY(1,1) NOT NULL,
	[brideName] [varchar](25) NOT NULL,
	[groomName] [varchar](25) NOT NULL,
	[weddingDate] [datetime] NOT NULL,
	[venue] [varchar](25) NOT NULL,
	[imageURL] [varchar](100) NOT NULL,
 CONSTRAINT [PK__weddings__1CE9A80D2A4271EA] PRIMARY KEY CLUSTERED 
(
	[weddingID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
SET IDENTITY_INSERT [dbo].[congratulations] ON 

INSERT [dbo].[congratulations] ([weddingID], [username], [congratsMessage], [messageID]) VALUES (1084, N'Badih', N'mabrouk!!', 13)
INSERT [dbo].[congratulations] ([weddingID], [username], [congratsMessage], [messageID]) VALUES (1084, N'badihchehab', N'mabrouk', 9)
INSERT [dbo].[congratulations] ([weddingID], [username], [congratsMessage], [messageID]) VALUES (1085, N'karl35', N'helloo', 11)
SET IDENTITY_INSERT [dbo].[congratulations] OFF
GO
SET IDENTITY_INSERT [dbo].[hasWeddings] ON 

INSERT [dbo].[hasWeddings] ([weddingID], [username], [ownershipID]) VALUES (1084, N'Badih', 1)
INSERT [dbo].[hasWeddings] ([weddingID], [username], [ownershipID]) VALUES (1085, N'badihchehab', 2)
SET IDENTITY_INSERT [dbo].[hasWeddings] OFF
GO
SET IDENTITY_INSERT [dbo].[moneyTransfer] ON 

INSERT [dbo].[moneyTransfer] ([weddingID], [username], [moneyAmount], [transactionID]) VALUES (1084, N'Badih', 500, 11)
INSERT [dbo].[moneyTransfer] ([weddingID], [username], [moneyAmount], [transactionID]) VALUES (1084, N'badihchehab', 400, 5)
INSERT [dbo].[moneyTransfer] ([weddingID], [username], [moneyAmount], [transactionID]) VALUES (1084, N'karl35', 250, 10)
SET IDENTITY_INSERT [dbo].[moneyTransfer] OFF
GO
INSERT [dbo].[userAttending] ([username], [weddingID]) VALUES (N'Badih', 1084)
GO
INSERT [dbo].[users] ([username], [email], [FirstName], [LastName], [UserPassword], [isAdmin]) VALUES (N'admin', N'admin@yahoo.com', N'Admin', N'Root', N'root', 1)
INSERT [dbo].[users] ([username], [email], [FirstName], [LastName], [UserPassword], [isAdmin]) VALUES (N'Badih', N'ki35@mail.aub.edu', N'Karl', N'Ibrahim', N'dawfegr', 0)
INSERT [dbo].[users] ([username], [email], [FirstName], [LastName], [UserPassword], [isAdmin]) VALUES (N'badihchehab', N'badihchehab@yahoo.com', N'Alice', N'Ha', N'password3435', 0)
INSERT [dbo].[users] ([username], [email], [FirstName], [LastName], [UserPassword], [isAdmin]) VALUES (N'karl35', N'karl35@gmail.com', N'Karl', N'Ibrahim', N'password', 0)
INSERT [dbo].[users] ([username], [email], [FirstName], [LastName], [UserPassword], [isAdmin]) VALUES (N'portaxe', N'dawd@inwejf.com', N'Badih', N'Chehab', N'dawdaw', 0)
GO
SET IDENTITY_INSERT [dbo].[weddings] ON 

INSERT [dbo].[weddings] ([weddingID], [brideName], [groomName], [weddingDate], [venue], [imageURL]) VALUES (1084, N'Jennifer', N'Josh', CAST(N'2021-05-02T17:54:00.000' AS DateTime), N'Venice', N'https://i.imgur.com/KBI4nhF.jpg')
INSERT [dbo].[weddings] ([weddingID], [brideName], [groomName], [weddingDate], [venue], [imageURL]) VALUES (1085, N'Yara', N'James', CAST(N'2021-06-01T08:00:00.000' AS DateTime), N'Tokyo', N'https://i.imgur.com/3Cqltzp.jpg')
SET IDENTITY_INSERT [dbo].[weddings] OFF
GO
/****** Object:  Index [UQ__congratu__4808B87254A88351]    Script Date: 5/4/2021 9:03:23 PM ******/
ALTER TABLE [dbo].[congratulations] ADD  CONSTRAINT [UQ__congratu__4808B87254A88351] UNIQUE NONCLUSTERED 
(
	[messageID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
/****** Object:  Index [UQ__hasWeddi__A8EC6842B5C83157]    Script Date: 5/4/2021 9:03:23 PM ******/
ALTER TABLE [dbo].[hasWeddings] ADD UNIQUE NONCLUSTERED 
(
	[ownershipID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
SET ANSI_PADDING ON
GO
/****** Object:  Index [usernameUnique]    Script Date: 5/4/2021 9:03:23 PM ******/
ALTER TABLE [dbo].[hasWeddings] ADD  CONSTRAINT [usernameUnique] UNIQUE NONCLUSTERED 
(
	[username] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
/****** Object:  Index [UQ__moneyTra__00D1E5030D1D75E5]    Script Date: 5/4/2021 9:03:23 PM ******/
ALTER TABLE [dbo].[moneyTransfer] ADD UNIQUE NONCLUSTERED 
(
	[transactionID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
SET ANSI_PADDING ON
GO
/****** Object:  Index [UQ__users__AB6E6164765D5408]    Script Date: 5/4/2021 9:03:23 PM ******/
ALTER TABLE [dbo].[users] ADD  CONSTRAINT [UQ__users__AB6E6164765D5408] UNIQUE NONCLUSTERED 
(
	[email] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
ALTER TABLE [dbo].[congratulations]  WITH CHECK ADD  CONSTRAINT [FK__congratul__weddi__06CD04F7] FOREIGN KEY([weddingID])
REFERENCES [dbo].[weddings] ([weddingID])
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[congratulations] CHECK CONSTRAINT [FK__congratul__weddi__06CD04F7]
GO
ALTER TABLE [dbo].[congratulations]  WITH CHECK ADD  CONSTRAINT [fk_username2] FOREIGN KEY([username])
REFERENCES [dbo].[users] ([username])
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[congratulations] CHECK CONSTRAINT [fk_username2]
GO
ALTER TABLE [dbo].[hasWeddings]  WITH CHECK ADD  CONSTRAINT [fk_username] FOREIGN KEY([username])
REFERENCES [dbo].[users] ([username])
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[hasWeddings] CHECK CONSTRAINT [fk_username]
GO
ALTER TABLE [dbo].[hasWeddings]  WITH CHECK ADD  CONSTRAINT [fk_weddingID] FOREIGN KEY([weddingID])
REFERENCES [dbo].[weddings] ([weddingID])
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[hasWeddings] CHECK CONSTRAINT [fk_weddingID]
GO
ALTER TABLE [dbo].[moneyTransfer]  WITH CHECK ADD FOREIGN KEY([weddingID])
REFERENCES [dbo].[weddings] ([weddingID])
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[moneyTransfer]  WITH CHECK ADD  CONSTRAINT [fk_username3] FOREIGN KEY([username])
REFERENCES [dbo].[users] ([username])
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[moneyTransfer] CHECK CONSTRAINT [fk_username3]
GO
ALTER TABLE [dbo].[userAttending]  WITH CHECK ADD  CONSTRAINT [fk_username4] FOREIGN KEY([username])
REFERENCES [dbo].[users] ([username])
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[userAttending] CHECK CONSTRAINT [fk_username4]
GO
ALTER TABLE [dbo].[userAttending]  WITH CHECK ADD  CONSTRAINT [fk_wedID] FOREIGN KEY([weddingID])
REFERENCES [dbo].[weddings] ([weddingID])
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[userAttending] CHECK CONSTRAINT [fk_wedID]
GO
USE [master]
GO
ALTER DATABASE [430PROJECT] SET  READ_WRITE 
GO
